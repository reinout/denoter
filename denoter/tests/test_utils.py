from pathlib import Path

from denoter import utils


def test_slugify():
    assert utils.slugify("Reinout is a great name!") == "reinout-is-a-great-name"


def test_denote_file_regex_1():
    assert utils.DENOTE_FILE_REGEX.search("20230717T143205--test-note.md")


def test_denote_file_regex_2():
    assert not utils.DENOTE_FILE_REGEX.search("20230717-test.md")


def test_is_denote_file():
    this_file = Path(__file__)
    assert not utils.is_denote_file(this_file)


def test_the_archive_file_regex_1():
    assert not utils.THE_ARCHIVE_FILE_REGEX.search("20230717T143205--test-note.md")


def test_the_archive_file_regex_2():
    assert utils.THE_ARCHIVE_FILE_REGEX.search(
        "202209191402-verschil-tussen-gezag-en-macht.md"
    )


def test_is_the_archive_file():
    this_file = Path(__file__)
    assert not utils.is_the_archive_file(this_file)


def test_timestamp_from_the_archive_file():
    result = utils.timestamp_from_the_archive(
        "202209191402-verschil-tussen-gezag-en-macht.md"
    )
    assert result.year == 2022
    assert result.hour == 14
