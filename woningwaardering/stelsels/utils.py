from decimal import Decimal
import importlib
import os
from datetime import date
from typing import Type, TypeVar

from loguru import logger
from prettytable import PrettyTable

from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)

T = TypeVar("T")


def import_class(module_path: str, class_naam: str, class_type: Type[T]) -> Type[T]:
    """
    Importeert een klasse uit een module.

    Parameters:
        module_path (str): Het pad naar de module waarin de klasse zich bevindt.
        class_naam (str): De naam van de klasse die geïmporteerd moet worden.
        class_type (Type[T]): Het verwachtte type van de klasse.

    Returns:
        Type[T]: De geïmporteerde klasse.

    Raises:
        ModuleNotFoundError: Als de module niet gevonden kan worden.
        AttributeError: Als de klasse van het opgegeven type niet gevonden kan worden in de module.
    """
    logger.debug(f"Importeer class '{class_naam}' uit '{module_path}'")
    try:
        module = importlib.import_module(module_path)
        class_: Type[T] = getattr(module, class_naam)
        if not issubclass(class_, class_type):
            raise TypeError(
                f"Class '{class_.__qualname__}' in '{class_.__module__}' is niet van het type '{class_type.__qualname__}'."
            )

    except ModuleNotFoundError as e:
        logger.error(f"Module {module_path} niet gevonden.", e)
        raise

    except AttributeError as e:
        logger.error(f"Class {class_naam} niet gevonden in: {module_path}.", e)
        raise

    return class_


def is_geldig(begindatum: date, einddatum: date, peildatum: date) -> bool:
    """
    Controleert of de peildatum valt tussen de begindatum en einddatum.

    Parameters:
        begindatum (date): De begindatum.
        einddatum (date): De einddatum.
        peildatum (date): De peildatum.

    Returns:
        bool: True als de peildatum tussen de begindatum en einddatum valt, anders False.
    """
    return begindatum <= peildatum <= einddatum


def vind_yaml_bestanden(directory: str) -> list[str]:
    """
    Zoekt alle YAML-bestanden in de opgegeven directory en de subdirectories.

    Parameters:
        directory (str): De hoofddirectory waarin naar YAML-bestanden wordt gezocht.

    Returns:
        list[str]: Een lijst met paden naar de gevonden YAML-bestanden.
    """
    logger.debug(f"Zoek naar YAML-bestanden in: {directory}")

    yaml_files = [
        os.path.join(root, file)
        for root, _, files in os.walk(directory)
        for file in files
        if file.endswith((".yaml", ".yml"))
    ]

    if not yaml_files:
        logger.error(f"Geen YAML-bestanden gevonden in: {directory}")
    return yaml_files


def naar_tabel(
    woningwaardering_resultaat: (
        WoningwaarderingResultatenWoningwaarderingResultaat
        | WoningwaarderingResultatenWoningwaarderingGroep
    ),
) -> PrettyTable:
    """
    Genereer een tabel met de details van een woningwaarderingresultaat.

    Parameters:
        woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat | WoningwaarderingResultatenWoningwaarderingGroep): Het object om de gegevens uit te halen

    Returns:
        PrettyTable: Een tabel met de gegevens van het woningwaarderingresultaat
    """
    table = PrettyTable()
    table.field_names = ["Groep", "Naam", "Aantal", "Meeteenheid", "Punten"]
    table.align["Groep"] = "l"
    table.align["Naam"] = "l"
    table.align["Aantal"] = "r"
    table.align["Meeteenheid"] = "l"
    table.align["Punten"] = "r"

    table.float_format = ".2"

    for woningwaardering_groep in (
        woningwaardering_resultaat.groepen or []
        if isinstance(
            woningwaardering_resultaat,
            WoningwaarderingResultatenWoningwaarderingResultaat,
        )
        else [woningwaardering_resultaat]
    ):
        for woningwaardering in woningwaardering_groep.woningwaarderingen or []:
            if (
                woningwaardering_groep.criterium_groep
                and woningwaardering_groep.criterium_groep.stelselgroep
                and woningwaardering.criterium
                and woningwaardering.criterium.meeteenheid
            ):
                table.add_row(
                    [
                        woningwaardering_groep.criterium_groep.stelselgroep.naam,
                        woningwaardering.criterium.naam,
                        woningwaardering.aantal,
                        woningwaardering.criterium.meeteenheid.naam,
                        woningwaardering.punten or "",
                    ]
                )
        if (
            woningwaardering_groep.criterium_groep
            and woningwaardering_groep.criterium_groep.stelselgroep
        ):
            table.add_row(
                [
                    woningwaardering_groep.criterium_groep.stelselgroep.naam,
                    "Subtotaal",
                    float(
                        sum(
                            [
                                Decimal(woningwaardering.aantal)
                                for woningwaardering in woningwaardering_groep.woningwaarderingen
                                or []
                                if woningwaardering.aantal is not None
                            ]
                        )
                    ),
                    "",
                    woningwaardering_groep.punten,
                ],
                divider=True,
            )
    if (
        isinstance(
            woningwaardering_resultaat,
            WoningwaarderingResultatenWoningwaarderingResultaat,
        )
        and woningwaardering_resultaat.stelsel
    ):
        table.add_row(
            [
                woningwaardering_resultaat.stelsel.naam,
                "Totaal",
                "",
                "",
                woningwaardering_resultaat.punten,
            ],
            divider=True,
        )

    return table
