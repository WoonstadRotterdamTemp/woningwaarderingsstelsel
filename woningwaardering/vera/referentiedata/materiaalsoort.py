from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Materiaalsoort(Referentiedatasoort):
    beton = Referentiedata(
        code="BET",
        naam="Beton",
    )

    bitumen = Referentiedata(
        code="BIT",
        naam="Bitumen",
    )

    cement = Referentiedata(
        code="CEM",
        naam="Cement",
    )

    gips = Referentiedata(
        code="GIP",
        naam="Gips",
    )

    glas = Referentiedata(
        code="GLA",
        naam="Glas",
    )

    grondstof = Referentiedata(
        code="GRO",
        naam="Grondstof",
    )

    hout = Referentiedata(
        code="HOU",
        naam="Hout",
    )

    isolatie = Referentiedata(
        code="ISO",
        naam="Isolatie",
    )

    kunststof = Referentiedata(
        code="KUN",
        naam="Kunststof",
    )

    metaal = Referentiedata(
        code="MET",
        naam="Metaal",
    )

    natuursteen = Referentiedata(
        code="NAT",
        naam="Natuursteen",
    )

    ntb = Referentiedata(
        code="NTB",
        naam="Ntb",
    )

    organisch = Referentiedata(
        code="ORG",
        naam="Organisch",
    )

    rubber = Referentiedata(
        code="RUB",
        naam="Rubber",
    )

    samengesteld = Referentiedata(
        code="SAM",
        naam="Samengesteld",
    )

    steenachtig = Referentiedata(
        code="STE",
        naam="Steenachtig",
    )
