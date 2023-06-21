import datetime
import logging
from dataclasses import dataclass
from pathlib import Path

from denoter import utils

# from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class DenoteMetadata:
    """This is what's needed to generate a filename"""

    title: str
    extension: str
    timestamp: datetime.datetime
    tags: list[str]


@dataclass
class BasicFileInfo:
    name: str
    extension: str
    creation_date: datetime.datetime


# @dataclass
# class DenoteFileInfo:
#     creation_date: datetime.datetime
#     slug: str
#     tags: list[str]


def extract_basic_file_info(file: Path) -> BasicFileInfo:
    name = file.stem  # Stem is the filename without the extension.
    extension = file.suffix  # Note: including the leading dot.

    # Multiple OSs have different ways of handling this.
    stats = file.stat()
    timestamp1 = stats.st_ctime
    timestamp2 = stats.st_mtime
    earliest = min([timestamp1, timestamp2])
    creation_date = datetime.datetime.fromtimestamp(earliest)
    result = BasicFileInfo(name=name, extension=extension, creation_date=creation_date)
    logger.debug("Basic file info extracted from %s: %s", file, result)
    return result


def metadata_from_file(file: Path) -> DenoteMetadata:
    info = extract_basic_file_info(file)
    # We assume for the moment we have nothing else.
    return DenoteMetadata(
        title=info.name,
        extension=info.extension,
        timestamp=info.creation_date,
        tags=[],
    )


def filename_from_metadata(metadata: DenoteMetadata) -> str:
    date = metadata.timestamp.strftime("%Y%m%dT%H%M%S")
    slugified = utils.slugify(metadata.title)
    name = "--".join([date, slugified])
    if metadata.tags:
        name = name + "__" + "_".join(metadata.tags)
    return name + metadata.extension
