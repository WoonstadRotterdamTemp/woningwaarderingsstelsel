from decimal import ROUND_HALF_UP, Decimal
from datetime import date
from importlib.resources import files
from itertools import chain

from loguru import logger
import pandas as pd


from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie

from woningwaardering.stelsels.utils import filter_dataframe_op_datum, naar_tabel

from woningwaardering.stelsels.zelfstandige_woonruimten import (
    OppervlakteVanVertrekken,
    OppervlakteVanOverigeRuimten,
)

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)

LOOKUP_TABEL_FOLDER = (
    "stelsels/zelfstandige_woonruimten/punten_voor_de_woz_waarde/lookup_tabellen"
)


class PuntenVoorDeWozWaarde2024(Stelselgroepversie):
    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.punten_voor_de_woz_waarde.value,
            )
        )

        if not woningwaardering_resultaat:
            raise ValueError("Geen woningwaardering resultaat gevonden")

        if not eenheid.bouwjaar:
            raise ValueError(f"Geen bouwjaar gevonden voor eenheid {eenheid.id}")

        minimum_punten = self._bereken_minimum_punten(
            eenheid.bouwjaar, woningwaardering_resultaat
        )

        woz_waarde = self.bepaal_woz_waarde(eenheid)

        if woz_waarde is None:
            woz_waarde = 0
            logger.warning("Geen WOZ-waarde gevonden")

        woz_waarde = self.minimum_woz_waarde(woz_waarde)

        df_woz_factor = pd.read_csv(
            files("woningwaardering").joinpath(f"{LOOKUP_TABEL_FOLDER}/woz_factor.csv")
        ).pipe(filter_dataframe_op_datum, self.peildatum)

        woningwaardering_groep.woningwaarderingen = []

        factor_onderdeel_I = df_woz_factor["Onderdeel I"].item()

        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Onderdeel I"
                ),
                punten=woz_waarde / factor_onderdeel_I,
            )
        )

        oppervlakte = self.bepaal_oppervlakte(eenheid, woningwaardering_resultaat)

        if oppervlakte == 0:
            raise ValueError(
                f"Kan geen punten voor de WOZ waarde berekenen omdat het totaal van de oppervlakte van stelselgroepen {Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam} en {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam} 0 is"
            )

        factor_onderdeel_II = df_woz_factor["Onderdeel II"].astype(float).item()

        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Onderdeel II"
                ),
                punten=woz_waarde / oppervlakte / factor_onderdeel_II,
            )
        )

        punten = max(
            minimum_punten,
            float(
                Decimal(
                    sum(
                        Decimal(str(woningwaardering.punten))
                        for woningwaardering in woningwaardering_groep.woningwaarderingen
                        or []
                        if woningwaardering.punten is not None
                    )
                ).quantize(Decimal("1"), ROUND_HALF_UP)
            ),
        )

        woningwaardering_groep.punten = punten
        return woningwaardering_groep

    def minimum_woz_waarde(self, woz_waarde: float) -> float:
        df_minimum_woz_waarde = pd.read_csv(
            files("woningwaardering").joinpath(
                f"{LOOKUP_TABEL_FOLDER}/minimum_woz_waarde.csv"
            )
        ).pipe(filter_dataframe_op_datum, self.peildatum)

        minimum_woz_waarde = df_minimum_woz_waarde["Minimumwaarde"].astype(float).item()

        if woz_waarde < minimum_woz_waarde:
            logger.info(
                f"WOZ-waarde {woz_waarde} is kleiner dan minimum {minimum_woz_waarde}, minimum wordt gebruikt"
            )
            woz_waarde = minimum_woz_waarde
        return woz_waarde

    def bepaal_oppervlakte(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> float:
        oppervlakte_stelsel_groepen = [
            groep
            for groep in (woningwaardering_resultaat.groepen or [])
            if (
                groep.criterium_groep is not None
                and groep.criterium_groep.stelselgroep is not None
                and groep.criterium_groep.stelselgroep.code
                in [
                    Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.code,
                    Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.code,
                ]
            )
        ] or [
            OppervlakteVanVertrekken(peildatum=self.peildatum).bereken(eenheid),
            OppervlakteVanOverigeRuimten(peildatum=self.peildatum).bereken(eenheid),
        ]

        oppervlakte = sum(
            (
                waardering.aantal
                for waardering in chain.from_iterable(
                    groep.woningwaarderingen or []
                    for groep in oppervlakte_stelsel_groepen
                )
                if waardering.aantal is not None
            ),
            start=0.0,
        )

        return oppervlakte

    def _bereken_minimum_punten(
        self,
        bouwjaar: int | None,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> float:
        """
        Berekent de minimum punten voor steselgroep WOZ-waarde.

        Args:
            bouwjaar (int | None): Het bouwjaar van de eenheid.
            woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat): woningwaardering resultaten.

        Returns:
            float: De minimum punten voor stelselgroep WOZ-waarde.
        """

        minimum_punten = 0

        if bouwjaar:
            if 2015 <= bouwjaar <= 2019:
                punten_critische_stelselgroepen = sum(
                    groep.punten or 0
                    for groep in woningwaardering_resultaat.groepen or []
                    if groep.punten
                    and groep.criterium_groep
                    and groep.criterium_groep.stelselgroep
                    and groep.criterium_groep.stelselgroep.code
                    and groep.criterium_groep.stelselgroep.code
                    in [
                        Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.code,
                        Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.code,
                        Woningwaarderingstelselgroep.verwarming.code,
                        Woningwaarderingstelselgroep.energieprestatie.code,
                        Woningwaarderingstelselgroep.keuken.code,
                        Woningwaarderingstelselgroep.sanitair.code,
                        Woningwaarderingstelselgroep.woonvoorzieningen_voor_gehandicapten.code,
                        Woningwaarderingstelselgroep.prive_buitenruimten.code,
                        Woningwaarderingstelselgroep.bijzondere_voorzieningen.code,  # Zorgwoning
                    ]
                )

                if punten_critische_stelselgroepen >= 110:
                    minimum_punten = 40
                    logger.info(
                        f"Minimum van 40 {Woningwaarderingstelselgroep.punten_voor_de_woz_waarde.naam}"
                    )

        return minimum_punten

    def bepaal_woz_waarde(self, eenheid: EenhedenEenheid) -> float | None:
        woz_waardepeildatum = date(self.peildatum.year - 1, 1, 1)

        woz_eenheid = next(
            (
                woz_eenheid
                for woz_eenheid in eenheid.woz_eenheden or []
                if woz_eenheid.waardepeildatum == woz_waardepeildatum
            ),
            None,
        )

        if woz_eenheid is None:
            return None

        return woz_eenheid.vastgestelde_waarde


if __name__ == "__main__":
    logger.enable("woningwaardering")

    woz = PuntenVoorDeWozWaarde2024()
    with open(
        "tests/data/zelfstandige_woonruimten/input/37101000032.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = woz.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = naar_tabel(woningwaardering_resultaat)

    print(tabel)
