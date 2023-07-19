import datetime
from pathlib import Path

import pytest

from denoter import core


@pytest.fixture
def metadata():
    return core.DenoteMetadata()


def test_metadata_empty_init():
    # DenoteMetadata should have defaults for everything.
    core.DenoteMetadata()


def test_extract_basic_filename_info(metadata):
    this_file = Path(__file__)
    core.extract_basic_filename_info(this_file, metadata)
    assert metadata.title == "test core"
    assert metadata.extension == ".py"


def test_estimate_file_creation_date(metadata):
    this_file = Path(__file__)
    core.estimate_file_creation_date(this_file, metadata)
    assert metadata.timestamp.year >= 2023


def test_reuse_the_archive_filename_timestamp(metadata):
    example = Path("202107201000-forward-movement.md")
    core.reuse_the_archive_filename_timestamp(example, metadata)
    assert metadata.timestamp.year == 2021
    assert metadata.timestamp.month == 7
    assert metadata.title == "forward movement"


def test_extract_denote_filename_info_1(metadata):
    example = Path("0-inbox/20230717T143205--test-note.md")
    core.extract_denote_filename_info(example, metadata)
    assert metadata.title == "test note"
    assert metadata.timestamp.year == 2023
    assert metadata.tags == set()


def test_extract_denote_filename_info_2(metadata):
    example = Path("0-inbox/20230717T143205--test-note__zettel.md")
    core.extract_denote_filename_info(example, metadata)
    assert metadata.title == "test note"
    assert metadata.timestamp.year == 2023
    assert metadata.tags == {"zettel"}


def test_extract_title_from_text_1(metadata):
    text = """Title on the first line

    Something more.
    """
    core.extract_title_from_text(text, metadata)
    assert metadata.title == "title on the first line"


def test_extract_title_from_text_2(metadata):
    text = """# Markdown title on the first line

    Something more.
    """
    core.extract_title_from_text(text, metadata)
    assert metadata.title == "markdown title on the first line"


def test_metadata_from_file(metadata):
    this_file = Path(__file__)
    metadata = core.metadata_from_file(this_file)
    assert metadata.title == "test core"
    assert metadata.extension == ".py"
    assert metadata.tags == set()


def test_metadata_from_file_2(metadata):
    this_file = Path(__file__)
    example = this_file.parent / "20230717T202456--title-on-the-first-line.md"
    metadata = core.metadata_from_file(example)
    assert metadata.title == "title on the first line"
    assert metadata.extension == ".md"
    assert metadata.tags == set()


def test_filename_from_metadata_1(metadata):
    metadata = core.DenoteMetadata(
        title="reinout is geweldig",
        extension=".txt",
        timestamp=datetime.datetime(year=1972, month=12, day=25),
        tags=set(),
    )
    metadata = core.filename_from_metadata(metadata)
    assert metadata == "19721225T000000--reinout-is-geweldig.txt"


def test_filename_from_metadata_2(metadata):
    metadata = core.DenoteMetadata(
        title="reinout is geweldig",
        extension=".txt",
        timestamp=datetime.datetime(year=1972, month=12, day=25),
        tags={"verjaardag", "feit"},
    )
    metadata = core.filename_from_metadata(metadata)
    assert metadata == "19721225T000000--reinout-is-geweldig__feit_verjaardag.txt"
