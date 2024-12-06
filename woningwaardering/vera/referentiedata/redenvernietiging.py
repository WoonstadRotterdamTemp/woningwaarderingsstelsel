from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Redenvernietiging(Referentiedatasoort):
    bedreiging = Referentiedata(
        code="DRE",
        naam="Bedreiging",
    )
    """
    De overeenkomst is nietig aangezien deze tot stand is gekomen onder bedreiging.
    """

    bedrog = Referentiedata(
        code="DRO",
        naam="Bedrog",
    )
    """
    De overeenkomst is nietig aangezien deze tot stand is gekomen  door bedrog.
    """

    dwaling = Referentiedata(
        code="DWA",
        naam="Dwaling",
    )
    """
    De overeenkomst is nietig aangezien deze tot stand is gekomen als het gevolg van
    dwaling.
    """

    misbruik = Referentiedata(
        code="MIS",
        naam="Misbruik",
    )
    """
    De overeenkomst is nietig aangezien deze tot stand is gekomen door misbruik van
    omstandigheden.
    """
