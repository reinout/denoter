import logging
from pathlib import Path

import typer
from typing_extensions import Annotated

from denoter import core

logger = logging.getLogger(__name__)
app = typer.Typer()


@app.command()
def main(
    files: Annotated[
        list[Path], typer.Argument(help="Files to rename.", dir_okay=False, exists=True)
    ],
    verbose: Annotated[bool, typer.Option(help="Be verbose.")] = False,
):
    log_level = logging.DEBUG and verbose or logging.INFO
    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")
    for file in files:
        print(core.metadata_from_file(file))
