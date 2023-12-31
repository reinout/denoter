# denoter

Introduction

Usage, etc.


## Aantekeningen

Naamgeving: `2023213123434234-iets-nuttigs.md` bevalt me niet
zo. `iets-nuttigs-RR0000001.md` bevalt me beter. Hoe kort kan zo'n `RR` tag
zijn? Niet alles hoeft het te hebben.


## Installation

We can be installed with:

    $ pip install denoter

(TODO: after the first release has been made)


## Development installation of this project itself

We use python's build-in "virtualenv" to get a nice isolated
directory. You only need to run this once:

    $ python3 -m venv .

A virtualenv puts its commands in the `bin` directory. So `bin/pip`,
`bin/pytest`, etc. Set up the dependencies like this:

    $ bin/pip install -e .[test]

There will be a script you can run like this:

    $ bin/denoter

It runs the `main()` function in `denoter/scripts.py`,
adjust that if necessary. The script is configured in
`TODO, MISSING NOW` (see `entry_points`).

In order to get nicely formatted python files without having to spend
manual work on it, get [pre-commit](https://pre-commit.com/) and install
it on this project:

    $ pre-commit install

Run the tests regularly with coverage:

    $ bin/pytest --cov

The tests are also run automatically [on "github
actions"](https://github.com/nens/denoter/actions) for
"main" and for pull requests. So don't just make a branch, but turn it into a
pull request right away. On your pull request page, you also automatically get
the feedback from the automated tests.

If you need a new dependency (like `requests`), add it in
`pyproject.toml` in `dependencies`. And update your local install with:

    $ bin/pip install -e .[test]
