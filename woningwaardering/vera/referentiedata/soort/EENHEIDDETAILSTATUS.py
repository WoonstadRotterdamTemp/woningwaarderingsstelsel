
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class EENHEIDDETAILSTATUS:

    verhuurd_antikraak = Referentiedata(
        code="ANT",
        naam="Verhuurd antikraak",
    )
    # verhuurd_antikraak = ("ANT", "Verhuurd antikraak")
    """
    De eenheid wordt verhuurd onder de voorwaarden van anti-kraak
    """

    bouwplannen = Referentiedata(
        code="BOU",
        naam="Bouwplannen",
    )
    # bouwplannen = ("BOU", "Bouwplannen")
    """
    Eenheid is in ontwikkeling, nog in de planfase
    """

    bruikleen = Referentiedata(
        code="BRU",
        naam="Bruikleen",
    )
    # bruikleen = ("BRU", "Bruikleen")
    """
    De eenheid wordt verhuurd onder een bruikleen constructie
    """

    wacht_op_energie_prestatie_advies = Referentiedata(
        code="EPA",
        naam="Wacht op Energie Prestatie Advies",
    )
    # wacht_op_energie_prestatie_advies = ("EPA", "Wacht op Energie Prestatie Advies")
    """
    Frictieleegstand, ontstaan doordat er nog gewacht wordt op de afgifte van een EPA
    label
    """

    mutatie = Referentiedata(
        code="MUT",
        naam="Mutatie",
    )
    # mutatie = ("MUT", "Mutatie")
    """
    Frictieleegstand wegens mutatieonderhoud. De eenheid is in exploitatie, maar niet
    verhuurd. Aansluitende verhuur is niet mogelijk omdat eerst nog onderhoud in de
    woning plaatsvindt.
    """

    wacht_op_nieuwe_huurder_niet_regulier = Referentiedata(
        code="NIB",
        naam="Wacht op nieuwe huurder - niet-regulier",
    )
    # wacht_op_nieuwe_huurder_niet_regulier = ("NIB", "Wacht op nieuwe huurder - niet-regulier")
    """
    Frictieleegstand, ontstaan doordat er nog geen nieuwe huurder is gevonden, waarbij
    geldt dat er sprake is van een niet-regulier toewijzingsproces of een niet-reguliere
    beoogd huurder. Het betreft de leegstand vanaf het moment waarop de woning klaar is
    voor verhuur (nadat eventueel mutatieonderhoud is afgerond) totdat de overeenkomst
    met een nieuwe, niet-reguliere, huurder ingaat.
    """

    nieuwbouw = Referentiedata(
        code="NIE",
        naam="Nieuwbouw",
    )
    # nieuwbouw = ("NIE", "Nieuwbouw")
    """
    Eenheid is in ontwikkeling, realisatie-/bouwfase is gestart
    """

    wacht_op_nieuwe_huurder_regulier = Referentiedata(
        code="NIH",
        naam="Wacht op nieuwe huurder - regulier",
    )
    # wacht_op_nieuwe_huurder_regulier = ("NIH", "Wacht op nieuwe huurder - regulier")
    """
    Frictieleegstand, ontstaan doordat er nog geen nieuwe huurder is gevonden, zonder
    dat daar een speciale oorzaak voor is (het reguliere matching proces duurt langer
    dan gewenst). Het betreft de leegstand vanaf het moment waarop de woning klaar is
    voor verhuur (nadat eventueel mutatieonderhoud is afgerond) totdat de overeenkomst
    met een nieuwe huurder ingaat.
    """

    oplevering = Referentiedata(
        code="OPL",
        naam="Oplevering",
    )
    # oplevering = ("OPL", "Oplevering")
    """
    Eenheid is in ontwikkeling, klaar voor oplevering
    """

    verhuurd_permanent = Referentiedata(
        code="PER",
        naam="Verhuurd permanent",
    )
    # verhuurd_permanent = ("PER", "Verhuurd permanent")
    """
    Doorlopend contract of voor onbepaalde tijd.
    """

    projectleegstand = Referentiedata(
        code="PRO",
        naam="Projectleegstand",
    )
    # projectleegstand = ("PRO", "Projectleegstand")
    """
    Leegstand doordat de eenheid deel uitmaakt van een onderhouds- of renovatieproject,
    waarbij de eenheid niet uit exploitatie wordt genomen
    """

    structurele_leegstand = Referentiedata(
        code="STR",
        naam="Structurele leegstand",
    )
    # structurele_leegstand = ("STR", "Structurele leegstand")
    """
    (Verwachte) Langdurige frictieleegstand, doordat vraag en aanbod niet op elkaar
    aansluiten
    """

    verhuurd_tijdelijk = Referentiedata(
        code="TIJD",
        naam="Verhuurd tijdelijk",
    )
    # verhuurd_tijdelijk = ("TIJD", "Verhuurd tijdelijk")
    """
    Huurcontract met beperkte looptijd (anders dan anti-kraak of onder een bruikleen
    constructie)
    """

    verkoop = Referentiedata(
        code="VEK",
        naam="Verkoop",
    )
    # verkoop = ("VEK", "Verkoop")
    """
    Leegstand omdat de eenheid op korte termijn verkocht zal worden, maar nog wel in
    exploitatie is.
    """

    vergunning_verleend = Referentiedata(
        code="VER",
        naam="Vergunning verleend",
    )
    # vergunning_verleend = ("VER", "Vergunning verleend")
    """
    Eenheid is in ontwikkeling, bouwvergunning is verleend
    """
