# ScrabbleBabble

[![Unit Tests](https://github.com/dvdl16/scrabblebabble/actions/workflows/python-unittest.yml/badge.svg)](https://github.com/dvdl16/scrabblebabble/actions/workflows/python-unittest.yml)
[![Linting](https://github.com/dvdl16/scrabblebabble/actions/workflows/linters.yml/badge.svg)](https://github.com/dvdl16/scrabblebabble/actions/workflows/linters.yml)

A tool to replace each word in a given sentence with another word starting with the same letter that is the same length.

## How do I run this?

### Using the live Demo version:

Go to [scrabblebabble.laarse.co.za](https://scrabblebabble.laarse.co.za) and have a shot at it.

*Deployed using [Fly.io](https://fly.io/), running `fly launch` created the files `Dockerfile`, `.dockerignore` and `fly.toml`*

### Using the shell

You would need to install [uv](https://docs.astral.sh/uv/), *the extremely fast Python package and project manager, written in Rust*.

**macOS and Linux:**
```shell
# Step 1: Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh 
# The installation script may be inspected before use with `curl -LsSf https://astral.sh/uv/install.sh | less`

# Step 2: Restart your shell or run `source $HOME/.cargo/env`

# Step 3: Clone the repository
git clone https://github.com/dvdl16/scrabblebabble.git

# Step 4: Run the program, with your sentence/words as arguments
uv run main.py hello world
```

**Windows**
```shell
# Step 1: Install uv
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Step 2: Restart your shell

# Step 3: Clone the repository
git clone https://github.com/dvdl16/scrabblebabble.git

# Step 4: Run the program, with your sentence/words as arguments
uv run main.py hello world
```

expect an answer like:
```shell
homed walty
```

### Using the local Web UI

Follow the same steps as *Using the shell* above, but run 
```shell
uv run wsgi.py
```
instead.

Open your browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see:

![web ui screenshot](docs/image.png)

## Development

To contribute features and fixes, clone the repository and use `uv`:

**macOS and Linux:**
```shell
# Step 1: Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh 
# The installation script may be inspected before use with `curl -LsSf https://astral.sh/uv/install.sh | less`

# Step 2: Restart your shell or run `source $HOME/.cargo/env`

# Step 3: Clone the repository
git clone https://github.com/dvdl16/scrabblebabble.git

# Step 4: Run uv sync
uv sync
```


We use [pre-commit](/home/dirk/Projects/Other/scrabblebabble/README.md) to run linting check before committing. First time setup may be required:

```shell
# Install the git hook scripts
pre-commit install

# (optional) Run against all the files
pre-commit run --all-files
```

## Tests

Run in your terminal, inside the project root
```shell
python -m unittest 
```

## Limitations, known bugs, wishlist

*Stuff I ran out of time for, or just thought would be valuable to consider*:

- Inconsistent Handling of Word Cases
    - Sometimes there may be unexpected lowercase results even if the input sentence contains capitalized words
- Non-Thread-Safety
- No Error Handling for Missing Words
  - Currently the app assumes that the provided word list contains words starting with all letters of the English alphabet
- Potentially Large In-Memory Word List
  - Perhaps we can implement lazy loading or on-demand caching for specific letter and length combinations
- Repeated Filtering of Available Words
  - Perhaps we can change the `WordlistProvider.process_lines()` to also use the word length as key, allowing for O(1) lookup for specific criteria
