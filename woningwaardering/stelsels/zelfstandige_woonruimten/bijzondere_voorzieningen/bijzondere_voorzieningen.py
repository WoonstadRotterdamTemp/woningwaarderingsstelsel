from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import bereken
from woningwaardering.stelsels.gedeelde_logica.bijzondere_voorzieningen.bijzondere_voorzieningen import (
    woningwaarderingen,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class BijzondereVoorzieningen(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.bijzondere_voorzieningen
        super().__init__(
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
        )

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel.value,
                stelselgroep=self.stelselgroep.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = list(
            woningwaarderingen(
                peildatum=self.peildatum,
                eenheid=eenheid,
                stelselgroepen_zonder_opslag=[
                    Woningwaarderingstelselgroep.prijsopslag_monumenten_en_nieuwbouw,
                    self.stelselgroep,
                ],
                woningwaardering_resultaat=woningwaardering_resultaat,
            )
        )

        punten = utils.rond_af_op_kwart(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            ),
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    bereken(
        class_=BijzondereVoorzieningen(),
        eenheid_input="tests/data/generiek/input/37101000032.json",
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    )
