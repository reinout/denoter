import datetime
from dataclasses import dataclass
from pathlib import Path

# from typing import Optional


@dataclass
class DenoteMetadata:
    title: str
    timestamp: datetime.datetime
    tags: list[str]
    extension: str


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
    print(creation_date)
    return BasicFileInfo(name=name, extension=extension, creation_date=creation_date)
