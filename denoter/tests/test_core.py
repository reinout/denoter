from pathlib import Path

from denoter import core


def test_extract_basic_file_info():
    this_file = Path(__file__)
    result = core.extract_basic_file_info(this_file)
    assert result.name == "test_core"
    assert result.extension == ".py"
