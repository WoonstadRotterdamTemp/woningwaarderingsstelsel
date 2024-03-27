from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Debiteursoort(Enum):
    debiteur_gemeente = Referentiedata(
        code="DGM",
        naam="Debiteur gemeente",
    )

    debiteur_overheid = Referentiedata(
        code="DOH",
        naam="Debiteur overheid",
    )

    huurdebiteur = Referentiedata(
        code="HUU",
        naam="Huurdebiteur",
    )

    overige_debiteur = Referentiedata(
        code="OVE",
        naam="Overige debiteur",
    )

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
