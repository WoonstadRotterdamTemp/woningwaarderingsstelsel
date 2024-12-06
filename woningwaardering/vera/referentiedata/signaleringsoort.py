from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Signaleringsoort(Referentiedatasoort):
    agressie = Referentiedata(
        code="AGR",
        naam="Agressie",
    )

    oneigenlijk_gebruik_woning = Referentiedata(
        code="ONE",
        naam="Oneigenlijk gebruik woning",
    )

    overlast = Referentiedata(
        code="OVE",
        naam="Overlast",
    )

    huurschuld = Referentiedata(
        code="SCH",
        naam="Huurschuld",
    )
