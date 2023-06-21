from pathlib import Path

from denoter import core


def test_basic_file_metadata():
    this_file = Path(__file__)
    result = core.basic_file_metadata(this_file)
    assert result.filename == "test_core.py"
