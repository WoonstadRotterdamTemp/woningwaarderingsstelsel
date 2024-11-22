from datetime import date

from woningwaardering.stelsels._dev_utils import bereken
from woningwaardering.stelsels.stelsel import Stelsel
from woningwaardering.stelsels.zelfstandige_woonruimten import (
    BijzondereVoorzieningen,
    Buitenruimten,
    Energieprestatie,
    GemeenschappelijkeParkeerruimten,
    GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen,
    Keuken,
    OppervlakteVanOverigeRuimten,
    OppervlakteVanVertrekken,
    PrijsopslagMonumentenEnNieuwbouw,
    PuntenVoorDeWozWaarde,
    Sanitair,
    VerkoelingEnVerwarming,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
)


class ZelfstandigeWoonruimten(Stelsel):
    def __init__(self, peildatum: date = date.today()) -> None:
        super().__init__(
            stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
            begindatum=date(2024, 7, 1),
            einddatum=date.max,
            peildatum=peildatum,
            stelselgroepen=[
                OppervlakteVanVertrekken,
                OppervlakteVanOverigeRuimten,
                VerkoelingEnVerwarming,
                Buitenruimten,
                Energieprestatie,
                Keuken,
                Sanitair,
                GemeenschappelijkeParkeerruimten,
                GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen,
                PuntenVoorDeWozWaarde,  # LET OP: deze stelselgroep dient als twee na laatste te worden uitgevoerd
                BijzondereVoorzieningen,  # LET OP: deze stelselgroep dient als een na laatste te worden uitgevoerd
                PrijsopslagMonumentenEnNieuwbouw,  # LET OP: deze stelselgroep dient als laatste te worden uitgevoerd
            ],
        )


if __name__ == "__main__":  # pragma: no cover
    bereken(
        instance=ZelfstandigeWoonruimten(),
        eenheid_input="tests/data/generiek/input/37101000032.json",
        strict=False,
    )
