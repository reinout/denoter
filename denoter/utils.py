import re
import unicodedata
from pathlib import Path

DENOTE_DATE_FORMAT = "%Y%m%dT%H%M%S"
DENOTE_FILE_REGEX = re.compile(
    r"""
    ^       # Start of string
    \d{8}   # yyyymmdd
    T       # T
    \d{6}   # hhmmss
    \-\-    # --
    """,
    re.VERBOSE,
)
THE_ARCHIVE_DATE_FORMAT = "%Y%m%d%H%M"
THE_ARCHIVE_FILE_REGEX = re.compile(
    r"""
    ^       # Start of string
    \d{12}  # yyyymmddhhmm
    \-      # -
    """,
    re.VERBOSE,
)
TEXTFILE_EXTENSIONS = [".md", ".rst", ".txt"]


def slugify(title: str) -> str:
    """Return slugified title

    It converts to lowercase, removes non-word characters (alphanumerics and
    underscores) and converts spaces to hyphens. Also strips leading and
    trailing whitespace.

    Copied from django via stackoverflow.

    """
    value = (
        unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    )
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    value = value.replace("_", " ")  # Extra compared to stackoverflow.
    return re.sub(r"[-\s]+", "-", value)


def slug_to_title(title: str) -> str:
    """Return title from a (possibly previously sluggified) title

    Its use is to compare a title, extracted from within a file, to the title
    extracted from a slugified filename.

    And also to take a filename, clean it up and turn it into something that
    looks like a title.

    """
    title = slugify(title)
    return title.replace("-", " ")


def is_denote_file(file: Path) -> bool:
    return bool(DENOTE_FILE_REGEX.search(file.name))


def is_the_archive_file(file: Path) -> bool:
    return bool(THE_ARCHIVE_FILE_REGEX.search(file.name))


def is_textfile(file: Path) -> bool:
    return file.suffix in TEXTFILE_EXTENSIONS
