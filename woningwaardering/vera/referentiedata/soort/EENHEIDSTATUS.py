
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class EENHEIDSTATUS:

    administratief = Referentiedata(
        code="ADM",
        naam="Administratief",
    )
    # administratief = ("ADM", "Administratief")
    """
    De eenheid wordt geëxploiteerd door een particulier of andere vastgoedbeheerder. De
    daadwerkelijke status van de eenheid is onbekend in de administratie van de
    corporatie
    """

    leegstand = Referentiedata(
        code="LEE",
        naam="Leegstand",
    )
    # leegstand = ("LEE", "Leegstand")
    """
    De eenheid is in exploitatie, maar niet verhuurd. Aansluitende verhuur is niet
    mogelijk omdat nog geen nieuwe huurder is gevonden of omdat de woning nog niet
    gereed is voor verhuur
    """

    in_ontwikkeling = Referentiedata(
        code="ONT",
        naam="In ontwikkeling",
    )
    # in_ontwikkeling = ("ONT", "In ontwikkeling")
    """
    De eenheid is (nog) niet in exploitatie omdat deze in ontwikkeling is. Gebruik
    eventueel een detailstatus om aan te geven in welke fase van het ontwikkelingsproces
    de eenheid zich bevindt
    """

    uit_exploitatie = Referentiedata(
        code="UIT",
        naam="Uit exploitatie",
    )
    # uit_exploitatie = ("UIT", "Uit exploitatie")
    """
    De eenheid is niet (meer) in exploitatie bij de corporatie. Gebruik in combinatie
    met Uit Exploitatiereden om te verantwoorden met welke reden de eenheid uit
    exploitatie is.
    """

    verhuurd = Referentiedata(
        code="VEH",
        naam="Verhuurd",
    )
    # verhuurd = ("VEH", "Verhuurd")
    """
    De eenheid is verhuurd voor bepaalde of onbepaalde duur
    """
