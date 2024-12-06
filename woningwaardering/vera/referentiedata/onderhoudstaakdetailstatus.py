from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.onderhoudstaakstatus import (
    Onderhoudstaakstatus,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Onderhoudstaakdetailstatus(Referentiedatasoort):
    klant_niet_aanwezig = Referentiedata(
        code="AFW",
        naam="Klant niet aanwezig",
        parent=Onderhoudstaakstatus.onderbroken,
    )
    """
    De taak is onderbroken omdat de klant niet aanwezig is
    """

    niet_de_juiste_discipline = Referentiedata(
        code="DIS",
        naam="Niet de juiste discipline",
        parent=Onderhoudstaakstatus.onderbroken,
    )
    """
    De taak is onderbroken omdat de vakman niet de juiste discipline heeft
    """

    inspectie_en_of_beoordeling_vereist = Referentiedata(
        code="INS",
        naam="Inspectie/beoordeling vereist",
        parent=Onderhoudstaakstatus.onderbroken,
    )
    """
    De taak is onderbroken omdat inspectie/beoordeling door inspecteur noodzakelijk is
    """

    materiaal_bestellen = Referentiedata(
        code="MAT",
        naam="Materiaal bestellen",
        parent=Onderhoudstaakstatus.onderbroken,
    )
    """
    De taak is onderbroken omdat materiaal besteld moet worden
    """

    offerte_benodigd = Referentiedata(
        code="OFF",
        naam="Offerte benodigd",
        parent=Onderhoudstaakstatus.onderbroken,
    )
    """
    De taak is onderbroken omdat een offerte nodig is
    """

    onvoldoende_tijd = Referentiedata(
        code="ONV",
        naam="Onvoldoende tijd",
        parent=Onderhoudstaakstatus.onderbroken,
    )
    """
    De taak is onderbroken omdat er onvoldoende tijd voor de vakman is
    """
