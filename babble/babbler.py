import random
from typing import Dict


class Babbler:
    available_words: str
    index_map: Dict

    def __init__(self) -> None:
        self.read_word_list()

    def read_word_list(self):
        """
        Read text file with list of words into memory
        """
        with open(
            "/home/dirk/Projects/Other/scrabblebabble/words_alpha.txt", "r"
        ) as file:
            self.available_words = file.read().splitlines()

            incumbent_letter = self.available_words[0][0]
            self.index_map = {incumbent_letter: 0}
            for index, word in enumerate(self.available_words):
                first_letter_of_word = word[0]
                if first_letter_of_word != incumbent_letter:
                    self.index_map[first_letter_of_word] = index
                    incumbent_letter = first_letter_of_word

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
            index_start = self.index_map[starting_letter]
            index_end = self.index_map[next_alphabet_letter(starting_letter)]

            same_length_available_words = [
                w
                for w in self.available_words[index_start:index_end]
                if len(w) == word_length
            ]

            new_sentence_list.append(random.choice(same_length_available_words))

            # TODO: handle z

        print(f"Received {sentence}")
        print(f"Returned {' '.join(new_sentence_list)}")

        return " ".join(new_sentence_list)


def next_alphabet_letter(s):
    return chr((ord(s.lower()) + 1 - 97) % 26 + 97)
