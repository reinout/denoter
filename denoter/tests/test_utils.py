from pathlib import Path

from denoter import utils


def test_slugify_1():
    assert utils.slugify("Reinout is a great name!") == "reinout-is-a-great-name"


def test_slugify_2():
    # Extra compared to the stackoverflow code: we want underscores zapped.
    assert utils.slugify("reinout_is-great") == "reinout-is-great"


def test_slug_to_title():
    assert utils.slug_to_title("reinout-is-great") == "reinout is great"


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
