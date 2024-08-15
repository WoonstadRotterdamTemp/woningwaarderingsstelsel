from pathlib import Path

import pytest

from tests.test_utils import assert_output_model, laad_specifiek_input_en_output_model
from woningwaardering.stelsels.zelfstandige_woonruimten import (
    PriveBuitenruimten,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep

# Get the absolute path to the current file
current_file_path = Path(__file__).absolute().parent


@pytest.fixture(params=[str(p) for p in (current_file_path / "output").rglob("*.json")])
def specifieke_input_en_output_model(request):
    output_file_path = request.param
    return laad_specifiek_input_en_output_model(
        current_file_path, Path(output_file_path)
    )


def test_PriveBuitenruimten(
    zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat
):
    prive_buitenruimten = PriveBuitenruimten()
    resultaat = prive_buitenruimten.bereken(
        zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat
    )
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)


def test_PriveBuitenruimten_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    eenheid_input, eenheid_output = zelfstandige_woonruimten_input_en_outputmodel
    prive_buitenruimten = PriveBuitenruimten(peildatum=peildatum)

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [prive_buitenruimten.bereken(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.prive_buitenruimten,
    )


def test_PriveBuitenruimten_specifiek_output(
    specifieke_input_en_output_model, peildatum
):
    eenheid_input, eenheid_output = specifieke_input_en_output_model
    prive_buitenruimten = PriveBuitenruimten(peildatum=peildatum)

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [prive_buitenruimten.bereken(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.prive_buitenruimten,
    )
