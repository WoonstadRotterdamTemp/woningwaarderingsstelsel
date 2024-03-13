from woningwaardering.vera.bvg.models import Referentiedata


class ONDERHOUDSBESTEDINGSOORT:
    materiaal = Referentiedata(
        code="MAT",
        naam="Materiaal",
    )
    """
    Verbruikt materiaal. Met name gebruikt bij afrekenwijze nacalculatie om het
    verbruikte materiaal door te belasten
    """

    onderbroken_tijd = Referentiedata(
        code="OND",
        naam="Onderbroken tijd",
    )
    """
    Wanneer een uitvoerende de werkzaamheden tijdelijk moet stilleggen (bijvoorbeeld
    voor het ophalen van materiaal) kan deze bestedingssoort gebruikt worden.
    """

    overige_kosten = Referentiedata(
        code="OVE",
        naam="Overige kosten",
    )
    """
    Overige bestedingen die niet onder één van de andere bestedingssoorten vallen
    """

    pakbonkosten = Referentiedata(
        code="PAK",
        naam="Pakbonkosten",
    )
    """
    Pakbonkosten
    """

    reistijd = Referentiedata(
        code="REI",
        naam="Reistijd",
    )
    """
    Reistijd van de uitvoerende
    """

    uitwerktijd = Referentiedata(
        code="UIT",
        naam="Uitwerktijd",
    )
    """
    Uitwerktijd van de uitvoerende na uitvoering werk. Kan gebruikt worden voor de tijd
    nadat de werkzaamheden door de uitvoerende zijn uitgevoerd en het moment waarop de
    uitvoerende beschikbaar is voor een vervolgtaak
    """

    vaste_taakprijs = Referentiedata(
        code="VAS",
        naam="Vaste taakprijs",
    )
    """
    Besteding is een vaste taakprijs conform een eenheidsprijzenlijst/prijzenboek. Bij
    een afrekenwijze Nacalculatie Eenheidsprijzen kan gebruik gemaakt worden van deze
    soort om de verschillende taakprijzen op te voeren.
    """

    werktijd = Referentiedata(
        code="WER",
        naam="Werktijd",
    )
    """
    Werktijd van de uitvoerende. Met name gebruikt bij afrekenwijze Nacalculatie om
    gewerkte uren door te belasten
    """
