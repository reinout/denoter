import datetime
from pathlib import Path

import pytest

from denoter import core


def test_extract_basic_file_info():
    this_file = Path(__file__)
    result = core.extract_basic_file_info(this_file)
    assert result.name == "test_core"
    assert result.extension == ".py"


def test_metadata_from_file():
    this_file = Path(__file__)
    result = core.metadata_from_file(this_file)
    assert result.title == "test_core"
    assert result.extension == ".py"
    assert result.tags == []


def test_metadata_from_file_2():
    this_file = Path(__file__)
    example = this_file.parent / "20230717T202456--title-on-the-first-line.md"
    result = core.metadata_from_file(example)
    assert result.title == "title on the first line"
    assert result.extension == ".md"
    assert result.tags == []


def test_extract_denote_file_info_1():
    example = Path("0-inbox/20230717T143205--test-note.md")
    result = core.extract_denote_file_info(example)
    assert result.title == "test note"
    assert result.extension == ".md"
    assert result.timestamp.year == 2023
    assert result.tags == []


def test_extract_denote_file_info_2():
    example = Path("0-inbox/20230717T143205--test-note__zettel.md")
    result = core.extract_denote_file_info(example)
    assert result.title == "test note"
    assert result.extension == ".md"
    assert result.timestamp.year == 2023
    assert result.tags == ["zettel"]


def test_filename_from_metadata_1():
    metadata = core.DenoteMetadata(
        title="reinout is geweldig",
        extension=".txt",
        timestamp=datetime.datetime(year=1972, month=12, day=25),
        tags=[],
    )
    result = core.filename_from_metadata(metadata)
    assert result == "19721225T000000--reinout-is-geweldig.txt"


def test_filename_from_metadata_2():
    metadata = core.DenoteMetadata(
        title="reinout is geweldig",
        extension=".txt",
        timestamp=datetime.datetime(year=1972, month=12, day=25),
        tags=["verjaardag", "feit"],
    )
    result = core.filename_from_metadata(metadata)
    assert result == "19721225T000000--reinout-is-geweldig__verjaardag_feit.txt"


def test_extract_textfile_info_1():
    this_file = Path(__file__)  # Not a .txt/.md
    with pytest.raises(AssertionError):
        core.extract_textfile_info(this_file)


def test_extract_textfile_info_2():
    this_file = Path(__file__)
    example_textfile = this_file.parent / "example.md"
    result = core.extract_textfile_info(example_textfile)
    assert result.title == "title on the first line"
