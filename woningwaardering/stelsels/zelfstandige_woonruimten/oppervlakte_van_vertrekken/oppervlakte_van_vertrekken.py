from datetime import date

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class OppervlakteVanVertrekken(Stelselgroep):
    def __init__(self, peildatum: date = date.today()) -> None:
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.oppervlakte_van_vertrekken
        super().__init__(peildatum=peildatum)


if __name__ == "__main__":
    ovv = OppervlakteVanVertrekken(peildatum=date(2024, 1, 1))
    with open(
        "./tests/data/input/zelfstandige_woonruimten/41164000002.json", "r+"
    ) as f:
        eenheid = EenhedenEenheid.model_validate_json(f.read())

    woningwaardering_resultaat = ovv.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = utils.naar_tabel(woningwaardering_resultaat)

    print(tabel)
