# A python project template.

## Setup

Clone the project and then:

* Edit `pyproject.toml`
    * `[tool.poetry]`: `name`, `description`, `packages`
    * `[tool.poetry.scripts]`
* Rename
    * `src/sample`
    * `tests/`
* Enable vscode plugins for workspace: _autoDocstring_, _Black Formatter_, _Even Better TOML, _Pylance_
* `poetry install`

## Documentation
* `poetry run sphinx-quickstart docs`
* In `docs/source/conf.py`:
[source,python]
    ````
    extensions = [
        "sphinx.ext.autodoc",
        "sphinx.ext.napoleon",
        "sphinx.ext.viewcode",
        "sphinx.ext.autosummary",
    ]
    ````
* Edit `docs/source/index.rst`:
    [source,rst]
    ````
    Welcome to Samples's documentation!
    ======================================

    .. toctree::
    :maxdepth: 4
    :caption: Contents:

    .. rubric:: Modules

    .. autosummary::
        :toctree: generated

        sample_with_docs.__init__
        sample_with_docs.__main__
        sammple_with_docs.file_functions

    Indices and tables
    ==================

    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`
    ````

## Commands
* `poetry run black src tests` -- format
* `poetry run ruff check --fix src tests` -- lint w/ autofix
* `poetry run ruff check src tests` -- lint
* `poetry run pytest ` -- test
* `poetry run coverage run -m pytest tests` -- coverage
    * `poetry run coverage report` -- print report
    * `poetry run coverage html` -- generate html report
* `poetry run sphinx-apidoc -f -o docs src` -- genrate package documentation
* `poetry run sphinx-apidoc -f -o docs/source src/sample` -- generate reST files from docstrings
* `poetry run sphinx-build -b html docs/source docs/build` -- generat HTML files from reST files
* `poetry run sample -s 3 4` -- run script
* `poetry run python -m main -s 3 4` -- run module
* `poetry run python src/main -s 3 4` -- run file directly
