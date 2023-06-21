import typer
import logging

logger = logging.getLogger(__name__)
app = typer.Typer()


@app.command()
def main(verbose: bool = False):
    log_level = logging.DEBUG and verbose or logging.INFO
    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")

    logging.info("iets")
