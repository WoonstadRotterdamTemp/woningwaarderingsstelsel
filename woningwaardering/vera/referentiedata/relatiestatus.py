from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Relatiestatus(Enum):
    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )
    """
    De relatie is een actieve relatie
    """

    inactief = Referentiedata(
        code="INA",
        naam="Inactief",
    )
    """
    De relatie is niet (meer) actief
    """

    slapend = Referentiedata(
        code="SLA",
        naam="Slapend",
    )
    """
    De relatie betreft een VvE (rechtspersoon) die een slapende status heeft
    """

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
