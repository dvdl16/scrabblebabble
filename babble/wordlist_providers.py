from collections import defaultdict
from io import TextIOWrapper
from typing import Dict, List, Union
from pathlib import Path

import requests


class WordlistProvider:
    available_words: Dict
    # Key is the starting letter, Value is the subset of words starting with this letter
    # e.g. {"a": ["apple", "aardvark"], "z": ["zero", "Zurich"]}

    def __init__(self) -> None:
        # Use list as default factory for new keys
        self.available_words = defaultdict(list)

    def process_lines(self, lines: Union[TextIOWrapper, List]):
        for line in lines:
            word = line.strip()
            self.available_words[word[0]].append(word)


class LocalFileWordlistProvider(WordlistProvider):
    def __init__(self, file_path: str = None) -> None:
        super().__init__()

        if not file_path:
            base_path = Path(__file__).parent
            file_path = (base_path / "../babble/assets/words_alpha.txt").resolve()

        # Open file
        with open(file_path, "r") as file:
            self.process_lines(file)


class HTTPFileWordListProvider(WordlistProvider):
    def __init__(self, url: str) -> None:
        super().__init__()

        response = requests.get(url)
        lines = response.text.splitlines()

        self.process_lines(lines)
