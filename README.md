# ScrabbleBabble

[![Unit Tests](https://github.com/dvdl16/scrabblebabble/actions/workflows/python-unittest.yml/badge.svg)](https://github.com/dvdl16/scrabblebabble/actions/workflows/python-unittest.yml)
[![Linting](https://github.com/dvdl16/scrabblebabble/actions/workflows/linters.yml/badge.svg)](https://github.com/dvdl16/scrabblebabble/actions/workflows/linters.yml)

## Development

`uv ......`

We use[pre-commit](/home/dirk/Projects/Other/scrabblebabble/README.md) to run linting check before committing. First time setup may be required:

```shell
# Install the git hook scripts
pre-commit install

# (optional) Run against all the files
pre-commit run --all-files
```

## Tests

```shell
python -m unittest 
```