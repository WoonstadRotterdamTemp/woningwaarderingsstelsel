from collections import defaultdict, namedtuple
from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.gedeelde_logica import waardeer_sanitair
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    Referentiedata,
    WoningwaarderingCriteriumSleutels,
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
from woningwaardering.vera.referentiedata.ruimtedetailsoort import Ruimtedetailsoort
from woningwaardering.vera.referentiedata.voorzieningsoort import Voorzieningsoort


class Sanitair(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.sanitair  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
        super().__init__(
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
        )

    @staticmethod
    def genereer_woningwaarderingen(
        ruimten: list[EenhedenRuimte],
        stelselgroep: Referentiedata,
    ) -> Iterator[tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]]:
        woningwaarderingen_voor_gedeeld = []
        # * tot een maximum van 1 punt per vertrek of overige ruimte m.u.v. de badkamer.
        # Op een adres met minimaal acht of meer onzelfstandige woonruimten geldt dit maximum niet voor maximaal één ruimte.
        # Dat betekent dat er voor adressen met acht of meer onzelfstandige woonruimten maximaal één ruimte mag zijn,
        # naast de badkamer, met meer dan één wastafel die voor waardering in aanmerking kom
        MaxCount = namedtuple("MaxCount", ["aantal_wastafels", "ruimte"])

        # Initialize with zero counts and no rooms
        max_wastafels = MaxCount(0, None)
        max_meerpersoonswastafels = MaxCount(0, None)

        for ruimte in ruimten:
            woningwaarderingen = list(
                waardeer_sanitair(
                    ruimte,
                    stelselgroep,
                    Woningwaarderingstelsel.onzelfstandige_woonruimten,
                )
            )
            # zoek het maximum aantal wastafels in een ruimte m.u.v. badkamer
            if ruimte.detail_soort not in [
                Ruimtedetailsoort.badkamer,
                Ruimtedetailsoort.badkamer_met_toilet,
                Ruimtedetailsoort.doucheruimte,
            ]:
                aantal_wastafels = sum(
                    [
                        woningwaardering.aantal or 0
                        for woningwaardering in woningwaarderingen
                        if (
                            woningwaardering.criterium
                            and woningwaardering.criterium.naam
                            and isinstance(woningwaardering.criterium.naam, str)
                            and f"{ruimte.naam} - {Voorzieningsoort.wastafel.naam}"
                            in woningwaardering.criterium.naam
                            and woningwaardering.aantal is not None
                            and isinstance(
                                Voorzieningsoort.meerpersoonswastafel.naam, str
                            )
                            and Voorzieningsoort.meerpersoonswastafel.naam
                            not in woningwaardering.criterium.naam
                        )
                    ]
                )
                if aantal_wastafels > max_wastafels.aantal_wastafels:
                    max_wastafels = MaxCount(aantal_wastafels, ruimte)

                aantal_meerpersoonswastafels = sum(
                    [
                        woningwaardering.aantal or 0
                        for woningwaardering in woningwaarderingen
                        if (
                            woningwaardering.criterium
                            and woningwaardering.criterium.naam
                            and isinstance(woningwaardering.criterium.naam, str)
                            and f"{ruimte.naam} - {Voorzieningsoort.meerpersoonswastafel.naam}"
                            in woningwaardering.criterium.naam
                        )
                    ]
                )
                if (
                    aantal_meerpersoonswastafels
                    > max_meerpersoonswastafels.aantal_wastafels
                ):
                    max_meerpersoonswastafels = MaxCount(
                        aantal_meerpersoonswastafels, ruimte
                    )
            woningwaarderingen_voor_gedeeld.append((ruimte, woningwaarderingen))

        # pas maximering toe voor wastafels en meerpersoonswastafels m.u.v. één ruimte,
        # de ruimte met de meeste wastafels/meerpersoonswastafels.
        woningwaarderingen_met_maximering = []
        for ruimte, woningwaarderingen in woningwaarderingen_voor_gedeeld:
            if (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten is not None
                and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten >= 8
                and max_wastafels.ruimte != ruimte
            ):
                for index, woningwaardering in enumerate(woningwaarderingen):
                    if (
                        woningwaardering.criterium
                        and woningwaardering.criterium.naam
                        and isinstance(woningwaardering.criterium.naam, str)
                        and isinstance(Voorzieningsoort.wastafel.naam, str)
                        and isinstance(Voorzieningsoort.meerpersoonswastafel.naam, str)
                        and f"{ruimte.naam} - {Voorzieningsoort.wastafel.naam}"
                        in woningwaardering.criterium.naam
                        and Voorzieningsoort.meerpersoonswastafel.naam
                        not in woningwaardering.criterium.naam
                        and woningwaardering.aantal is not None
                        and woningwaardering.aantal > 1
                    ):
                        logger.info(
                            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft {woningwaardering.aantal} wastafels. Maximaal 1 punt voor wastafels."
                        )
                        woningwaarderingen.insert(
                            index + 1,
                            (
                                WoningwaarderingResultatenWoningwaardering(
                                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                        naam=f"{ruimte.naam} - Max 1 punt voor {Voorzieningsoort.wastafel.naam}",
                                    ),
                                    punten=float(
                                        utils.rond_af(
                                            1 - woningwaardering.aantal * 1,
                                            decimalen=2,
                                        )
                                    ),
                                )
                            ),
                        )
            if (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten is not None
                and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten >= 8
                and max_meerpersoonswastafels.ruimte != ruimte
            ):
                for index, woningwaardering in enumerate(woningwaarderingen):
                    if (
                        woningwaardering.criterium
                        and woningwaardering.criterium.naam
                        and isinstance(woningwaardering.criterium.naam, str)
                        and isinstance(Voorzieningsoort.meerpersoonswastafel.naam, str)
                        and f"{ruimte.naam} - {Voorzieningsoort.meerpersoonswastafel.naam}"
                        in woningwaardering.criterium.naam
                        and woningwaardering.aantal is not None
                        and woningwaardering.aantal > 1
                    ):
                        logger.info(
                            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft {woningwaardering.aantal} meerpersoonswastafels. Maximaal 1,5 punt voor meerpersoonswastafels."
                        )
                        woningwaarderingen.insert(
                            index + 1,
                            WoningwaarderingResultatenWoningwaardering(
                                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                    naam=f"{ruimte.naam} - Max 1.5 punt voor {Voorzieningsoort.meerpersoonswastafel.naam}",
                                ),
                                punten=float(
                                    utils.rond_af(
                                        Decimal("1.5")
                                        - (
                                            Decimal(str(woningwaardering.aantal))
                                            * Decimal("1.5")
                                        ),
                                        decimalen=2,
                                    )
                                ),
                            ),
                        )
            woningwaarderingen_met_maximering.append((ruimte, woningwaarderingen))

        gedeeld_met_counter: defaultdict[int, Decimal] = defaultdict(Decimal)
        for ruimte, woningwaarderingen in woningwaarderingen_met_maximering:
            for woningwaardering in woningwaarderingen:
                woningwaardering.punten = float(
                    utils.rond_af(
                        (Decimal(str(woningwaardering.punten or 0)))
                        / Decimal(
                            str(
                                (
                                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
                                    or 1
                                )
                            )
                        ),
                        decimalen=2,
                    )
                )
                if (
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten is not None
                    and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten > 1
                ):
                    if woningwaardering.criterium:
                        woningwaardering.criterium.bovenliggende_criterium = WoningwaarderingCriteriumSleutels(
                            id=f"{stelselgroep.name}_gedeeld_met_{ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten}_onzelfstandige_woonruimten"
                        )
                    gedeeld_met_counter[
                        ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
                    ] += Decimal(str(woningwaardering.punten or 0))
                else:
                    if woningwaardering.criterium:
                        woningwaardering.criterium.bovenliggende_criterium = (
                            WoningwaarderingCriteriumSleutels(
                                id=f"{stelselgroep.name}_prive"
                            )
                        )
                    gedeeld_met_counter[1] += Decimal(str(woningwaardering.punten or 0))

                yield ruimte, woningwaardering

        # bereken de som van de woningwaarderingen per het aantal gedeelde onzelfstandige woonruimten
        for aantal_onz, punten in gedeeld_met_counter.items():
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=f"Totaal (gedeeld met {aantal_onz})"
                if aantal_onz > 1
                else "Totaal (privé)",
                id=f"{stelselgroep.name}_gedeeld_met_{aantal_onz}_onzelfstandige_woonruimten"
                if aantal_onz > 1
                else f"{stelselgroep.name}_prive",
            )
            woningwaardering.punten = float(utils.rond_af_op_kwart(punten))
            yield ruimte, woningwaardering

    def waardeer(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel,
                stelselgroep=self.stelselgroep,
            )
        )
        woningwaardering_groep.woningwaarderingen = []

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if not utils.gedeeld_met_eenheden(ruimte)
        ]

        waarderingen_met_ruimten = list(
            Sanitair.genereer_woningwaarderingen(ruimten, self.stelselgroep)
        )
        woningwaardering_groep.woningwaarderingen.extend(
            [waardering for _, waardering in waarderingen_met_ruimten]
        )

        # er is hier al op kwart afgerond
        woningwaardering_groep.punten = float(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
                and woningwaardering.criterium is not None
                and woningwaardering.criterium.bovenliggende_criterium is None
            )
        )

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=Sanitair(),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
