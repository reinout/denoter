import datetime
import logging
from dataclasses import dataclass
from pathlib import Path

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
    creation_date = datetime.datetime.fromtimestamp(file.stat().st_ctime)
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
