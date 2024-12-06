from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Boekjaarperiodesoort(Referentiedatasoort):
    boekjaarperiodesoort_4_weken = Referentiedata(
        code="4WE",
        naam="4-weken",
    )
    """
    Deel van een kalenderjaar met een vaste duur van 4 aaneengesloten kalenderweken.
    """

    halfjaar = Referentiedata(
        code="HLJ",
        naam="Halfjaar",
    )
    """
    Deel van een kalenderjaar met een vaste duur van 6 aaneengesloten kalendermaanden.
    """

    jaar = Referentiedata(
        code="JAR",
        naam="Jaar",
    )
    """
    Periode die uitgaat van een kalenderjaar.
    """

    kwartaal = Referentiedata(
        code="KWA",
        naam="Kwartaal",
    )
    """
    Deel van een kalenderjaar met een vaste duur van 3 aaneengesloten kalandermaanden.
    """

    maand = Referentiedata(
        code="MAA",
        naam="Maand",
    )
    """
    Deel van een kalenderjaar met een vaste duur van 1 kalendermaand.
    """

    tertiaal = Referentiedata(
        code="TER",
        naam="Tertiaal",
    )
    """
    Deel van een kalenderjaar met een vaste duur van 4 aaneengesloten kalandermaanden.
    """

    week = Referentiedata(
        code="WEE",
        naam="Week",
    )
    """
    Deel van een kalenderjaar met een vaste duur van 3 aaneengesloten kalendermaanden.
    """
