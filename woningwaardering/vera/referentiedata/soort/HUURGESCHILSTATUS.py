from woningwaardering.vera.bvg.models import Referentiedata


class HUURGESCHILSTATUS:
    afgewezen = Referentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    """
    Het huurgeschil is afgewezen, en daarmee tevens afgehandeld
    """

    in_behandeling = Referentiedata(
        code="INB",
        naam="In behandeling",
    )
    """
    Het huurgeschil is (nog) in behandeling
    """

    toegekend = Referentiedata(
        code="TOE",
        naam="Toegekend",
    )
    """
    Het huurgeschil is toegekend, en daarmee tevens afgehandeld
    """
