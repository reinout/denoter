import datetime
import logging
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path

from denoter import utils

# from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class DenoteMetadata:
    """This is what's needed to generate a filename"""

    title: str = ""
    extension: str = ""
    timestamp: datetime.datetime = field(default_factory=datetime.datetime.now)
    tags: set[str] = field(default_factory=set)


def extract_basic_filename_info(file: Path, metadata: DenoteMetadata):
    """Update metadata with the basic file info"""
    metadata.title = utils.slug_to_title(file.stem)
    # ^^^ Stem is the filename without the extension.
    metadata.extension = file.suffix
    # ^^^ Note: including the leading dot.


def estimate_file_creation_date(file: Path, metadata: DenoteMetadata):
    # Multiple OSs have different ways of handling this.
    stats = file.stat()
    timestamp1 = stats.st_ctime
    timestamp2 = stats.st_mtime
    earliest = min([timestamp1, timestamp2])
    creation_date = datetime.datetime.fromtimestamp(earliest)
    logger.debug("Estimated creation date: %s", creation_date)
    metadata.timestamp = creation_date


def reuse_the_archive_filename_timestamp(file: Path, metadata: DenoteMetadata):
    if not utils.is_the_archive_file(file):
        return
    id, title = file.stem.split("-", 1)
    metadata.title = utils.slug_to_title(title)
    metadata.timestamp = datetime.datetime.strptime(id, utils.THE_ARCHIVE_DATE_FORMAT)
    logger.debug("Reusing 'the archive' timestamp: %s", metadata.timestamp)


def extract_denote_filename_info(file: Path, metadata: DenoteMetadata):
    if not utils.is_denote_file(file):
        return

    name = file.stem  # Stem is the filename without the extension.
    id, remainder = name.split("--")
    metadata.timestamp = datetime.datetime.strptime(id, utils.DENOTE_DATE_FORMAT)

    if "__" in remainder:
        title, tag_string = remainder.split("__")
        tags = tag_string.split("_")
    else:
        title = remainder
        tags = []
    metadata.title = utils.slug_to_title(title)
    metadata.tags = set(tags)

    logger.debug("Denote file info extracted from %s: %s", file, metadata)


def extract_title_from_text(text: str, metadata: DenoteMetadata):
    lines = text.split("\n")
    title = lines[0]
    if title.startswith("# "):  # Markdown
        title.lstrip("# ")
    metadata.title = utils.slug_to_title(title)
    logger.debug("Extracted title from the contents: %s", metadata.title)


# We define the constants here as the functions are available now. It is used
# as parameters to the `metadata_from_file()` function for ease of testing.
FILE_EXTRACTORS = [
    extract_basic_filename_info,
    estimate_file_creation_date,
    reuse_the_archive_filename_timestamp,
    extract_denote_filename_info,
]
TEXT_EXTRACTORS = [extract_title_from_text]


def metadata_from_file(
    file: Path, file_extractors=FILE_EXTRACTORS, text_extractors=TEXT_EXTRACTORS
) -> DenoteMetadata:
    metadata = DenoteMetadata()
    for file_extractor in file_extractors:
        file_extractor(file, metadata)
    if utils.is_textfile(file):
        content = file.read_text()
        for text_extractor in text_extractors:
            text_extractor(content, metadata)
    return metadata


def filename_from_metadata(metadata: DenoteMetadata) -> str:
    id = metadata.timestamp.strftime(utils.DENOTE_DATE_FORMAT)
    slugified = utils.slugify(metadata.title)
    name = "--".join([id, slugified])
    if metadata.tags:
        name = name + "__" + "_".join(sorted(metadata.tags))
    return name + metadata.extension
