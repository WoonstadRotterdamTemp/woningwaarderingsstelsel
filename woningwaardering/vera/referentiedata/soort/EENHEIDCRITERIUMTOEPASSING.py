from woningwaardering.vera.bvg.models import Referentiedata


class EENHEIDCRITERIUMTOEPASSING:
    selectie = Referentiedata(
        code="SEL",
        naam="Selectie",
    )
    """
    Selectiecriteria die worden gebruikt om de passendheid van een woningzoekende voor
    de eenheid te bepalen.
    """

    sortering = Referentiedata(
        code="SOR",
        naam="Sortering",
    )
    """
    Sorteercriteria die worden gebruikt om de positie van een woningzoekende voor de
    eenheid te bepalen.
    """
