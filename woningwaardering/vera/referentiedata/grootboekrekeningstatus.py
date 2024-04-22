from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Grootboekrekeningstatus(Enum):
    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )

    geblokkeerd = Referentiedata(
        code="BLK",
        naam="Geblokkeerd",
    )

    historisch = Referentiedata(
        code="HIS",
        naam="Historisch",
    )

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("De code van een Referentiedata object mag niet None zijn.")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
