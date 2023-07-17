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
