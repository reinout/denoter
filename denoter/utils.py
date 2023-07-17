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
    return re.sub(r"[-\s]+", "-", value)


def unslugify(title: str) -> str:
    """Return title from a previously sluggified title

    Its use is to compare a title, extracted from within a file, to the title
    extracted from a slugified filename.

    """
    return title.replace("-", " ")


def is_denote_file(file: Path) -> bool:
    return bool(DENOTE_FILE_REGEX.search(file.name))
