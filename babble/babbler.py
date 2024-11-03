import random
from typing import Dict
import logging

from babble.wordlist_providers import (
    HTTPFileWordListProvider,
    LocalFileWordlistProvider,
    WordlistProvider,
)


class Babbler:
    available_words: Dict
    index_map: Dict
    wordlist_provider: WordlistProvider

    def __init__(self) -> None:
        self.read_word_list()

    def read_word_list(self):
        """
        Read text file with list of words into memory
        """
        # First try to get original word list, else fallback to local copy
        try:
            self.wordlist_provider = HTTPFileWordListProvider(
                url="https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words_alpha.txt"
            )
        except Exception:
            logging.warning(
                "Failed to retrieve word list via web. Falling back to local copy"
            )
            self.wordlist_provider = LocalFileWordlistProvider()

        self.available_words = self.wordlist_provider.available_words

    def get_new_words(self, sentence: str) -> str:
        """
        Given a sentence, will replace each word in the sentence with another word starting with the same letter that is the same length.
        If a particular word can't be found that matches the criteria above, then the original word should be returned.
        Another requirement is that the same input should return a different output each time.
        """
        new_sentence_list = []

        words = sentence.split()
        for word in words:
            starting_letter = word[0].lower()
            word_length = len(word)

            # Get subset of possible choices, based on word length
            same_length_available_words = [
                w
                for w in self.available_words[starting_letter]
                if len(w) == word_length and w != word
            ]

            if len(same_length_available_words) == 0:
                # Return the same word if no alternatives are available
                choice = word
            else:
                # Make sure to not return the same word if others are available
                while (
                    choice := random.choice(same_length_available_words).lower()
                ) == word.lower():
                    pass

            new_sentence_list.append(choice)

        logging.info(f"Received {sentence}")
        logging.info(f"Returned {' '.join(new_sentence_list)}")

        return " ".join(new_sentence_list)
