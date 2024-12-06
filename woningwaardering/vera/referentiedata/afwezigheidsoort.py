from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Afwezigheidsoort(Referentiedatasoort):
    adoptieverlof = Referentiedata(
        code="ADO",
        naam="Adoptieverlof",
    )

    bijzonder_verlof = Referentiedata(
        code="BIJ",
        naam="Bijzonder verlof",
    )

    calamiteitenverlof = Referentiedata(
        code="CAL",
        naam="Calamiteitenverlof",
    )

    geschorst = Referentiedata(
        code="GES",
        naam="Geschorst",
    )

    non_actief = Referentiedata(
        code="NON",
        naam="Non-actief",
    )

    onbetaald_verlof = Referentiedata(
        code="ONB",
        naam="Onbetaald verlof",
    )

    ouderschapsverlof = Referentiedata(
        code="OUD",
        naam="Ouderschapsverlof",
    )

    verlof_regulier = Referentiedata(
        code="VER",
        naam="Verlof (regulier)",
    )

    ziek = Referentiedata(
        code="ZIE",
        naam="Ziek",
    )

    zorgverlof = Referentiedata(
        code="ZOR",
        naam="Zorgverlof",
    )

    zwangerschapsverlof = Referentiedata(
        code="ZWA",
        naam="Zwangerschapsverlof",
    )
