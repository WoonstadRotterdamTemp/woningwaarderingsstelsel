from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Inspectierapportstatus(Enum):
    concept = Referentiedata(
        code="CON",
        naam="Concept",
    )

    definitief = Referentiedata(
        code="DEF",
        naam="Definitief",
    )

    getekend = Referentiedata(
        code="GET",
        naam="Getekend",
    )

    ter_review = Referentiedata(
        code="REV",
        naam="Ter review",
    )

    vervallen = Referentiedata(
        code="VAL",
        naam="Vervallen",
    )

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
