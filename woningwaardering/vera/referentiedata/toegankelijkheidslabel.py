from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Toegankelijkheidslabel(Enum):
    gelijkvloerse_woning = Referentiedata(
        code="GEL",
        naam="Gelijkvloerse woning",
    )
    """
    Label dat aangeeft dat de woning intern toegankelijk is voor minder validen: de
    belangrijkste vertrekken (woonkamer, keuken, toilet, badkamer en één slaapkamer)
    zijn bereikbaar zonder gebruik te hoeven maken van een trap (d.w.z. gelegen op
    één verdieping laag of meerdere verdiepingslagen die zonder trap - maar
    bijvoorbeeld met traplift - bereikbaar zijn). Een gelijkvloerse woning voldoet
    niet per definitie aan het criterium &#39;nultredenwoning&#39; omdat de woning daarvoor
    ook extern toegankelijk moet zijn voor minder validen.
    """

    rollatorwoning = Referentiedata(
        code="ROA",
        naam="Rollatorwoning",
    )
    """
    Label dat aangeeft dat de woning zowel intern als extern toegankelijk is met een
    rollator. De woning voldoet hiermee automatisch aan het criterium
    &#39;nultredenwoning&#39;, maar is niet per definitie ook een &#39;rolstoelwoning&#39; omdat er
    bijvoorbeeld drempels aanwezig kunnen zijn.
    """

    rolstoelwoning = Referentiedata(
        code="ROL",
        naam="Rolstoelwoning",
    )
    """
    Label dat aangeeft dat de woning zowel intern als extern toegankelijk is, met een
    rolstoel. De woning voldoet hiermee automatisch aan het criterium
    &#39;nultredewoning&#39;. Een rolstoelwoning voldoet per definitie ook aan het label
    Rollatorwoning, maar is niet per definitie ook een &#39;extra ruime rolstoelwoning&#39;.
    """

    extra_ruime_rolstoelwoning = Referentiedata(
        code="RUI",
        naam="Extra ruime rolstoelwoning",
    )
    """
    Label dat aangeeft dat de woning zowel intern als extern toegankelijk is, met een
    grote (elektrische) rolstoel. De woning voldoet hiermee automatisch aan het
    criterium &#39;nultredenwoning&#39;. Een extra ruime rolstoelwoning voldoet per
    definitie ook aan het label Rolstoelwoning.
    """

    woning_zonder_bijzondere_toegankelijkheid = Referentiedata(
        code="ZON",
        naam="Woning zonder bijzondere toegankelijkheid",
    )

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
