import sys
from babble.babbler import Babbler


def main(sentence: str):
    processor = Babbler()
    print(processor.get_new_words(sentence))


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        raise ValueError("Please specify an argument")
    main(sentence=" ".join(args))
