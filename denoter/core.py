import datetime
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class DenoteMetadata:
    title: str
    timestamp: datetime.datetime
    tags: List[str]


@dataclass
class BasicFileMetadata:
    filename: str
    creation_date: datetime.datetime


@dataclass
class DenoteFileMetadata:
    creation_date: datetime.datetime
    slug: str
    tags: List[str]


def basic_file_metadata(file: Path) -> BasicFileMetadata:
    filename = file.name
    creation_date = datetime.datetime.fromtimestamp(file.stat().st_ctime)
    print(creation_date)
    return BasicFileMetadata(filename=filename, creation_date=creation_date)
