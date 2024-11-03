import unittest

from babble.babbler import Babbler


class TestBabblerIntegration(unittest.TestCase):
    def setUp(self):
        self.processor = Babbler()

    def test_babbler_rules_happy_path(self):
        """
        Test if Babbler to transform sentences correctly
        """
        test_cases = [
            "hello world",
            "foo bar",
            "not hot dog",
            "you are incorrigible",
            "zebra is an equus quagga",
        ]

        for sentence in test_cases:
            with self.subTest(sentence=sentence):
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

    def test_babbler_returns_the_same_word_if_non_found(self):
        """
        Test if Babbler to transform sentences correctly
        """
        sentence = "nonexistingverylongword probably does not have an alternative"
        result = self.processor.get_new_words(sentence)

        self.assertEqual(
            result.split()[0],
            "nonexistingverylongword",
            "If a particular word can't be found that matches the criteria, then the original word should be returned.",
        )


if __name__ == "__main__":
    unittest.main()
