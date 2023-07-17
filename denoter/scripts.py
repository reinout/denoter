import logging
from pathlib import Path

import typer
from typing_extensions import Annotated

from denoter import core
from denoter import utils

logger = logging.getLogger(__name__)
app = typer.Typer()


# See https://jacobian.org/til/common-arguments-with-typer/
@app.callback()
def main(
    ctx: typer.Context,
    verbose: Annotated[bool, typer.Option(help="Be verbose.")] = False,
):
    log_level = logging.DEBUG and verbose or logging.INFO
    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")


@app.command()
def ingest(
    ctx: typer.Context,
    files: Annotated[
        list[Path], typer.Argument(help="Files to rename.", dir_okay=False, exists=True)
    ],
):
    for file in files:
        if utils.is_denote_file(file):
            logger.warn("Already a denote file, ignoring: %s", file)
            continue
        metadata = core.metadata_from_file(file)
        new_filename = core.filename_from_metadata(metadata)
        new_filepath = file.parent / new_filename
        rename = typer.confirm(f"Rename {file} to {new_filename}?")
        if rename:
            file.rename(new_filepath)
            logger.info("Renamed %s to %s", file, new_filepath)


@app.command()
def update_title(
    ctx: typer.Context,
    files: Annotated[
        list[Path], typer.Argument(help="Files to rename.", dir_okay=False, exists=True)
    ],
):
    for file in files:
        if not utils.is_denote_file(file):
            logger.warn("Not a denote file, ignoring: %s", file)
            continue
        metadata = core.metadata_from_file(file)

        new_filename = core.filename_from_metadata(metadata)
        if new_filename == file.name:
            logger.info("Title of %s is still the same", file)
            continue

        new_filepath = file.parent / new_filename
        rename = typer.confirm(f"Rename {file} to {new_filename}?")
        if rename:
            file.rename(new_filepath)
            logger.info("Renamed %s to %s", file, new_filepath)
