import unittest

from babble.babbler import Babbler


class TestBabblerIntegration(unittest.TestCase):
    def setUp(self):
        self.processor = Babbler()

    def test_babbler_rules(self):
        """
        Test if Babbler to transform sentences correctly
        """
        sentence = "hello world"
        result = self.processor.get_new_words(sentence)

        self.assertTrue(
            len(result.split()) == len(sentence.split()),
            "Sentence should have the same number of words.",
        )

        for result_word, sentence_word in zip(result.split(), sentence.split()):
            self.assertNotEqual(
                result_word.lower(), sentence_word, "Words should be repalced."
            )

        self.assertEqual(
            [result_word[0] for result_word in result.split()],
            [sentence_word[0] for sentence_word in sentence.split()],
            "Replaced words should start with the same letter as original words.",
        )

        self.assertEqual(
            [len(result_word) for result_word in result.split()],
            [len(sentence_word) for sentence_word in sentence.split()],
            "Replaced words should be the same length as original words.",
        )


if __name__ == "__main__":
    unittest.main()
