from unittest import TestCase, main
from generate_phrase_hw import generate_phrase


class TestGeneratePhrase(TestCase):

    # True Cases
    def test_true_single_char(self):
        self.assertTrue(generate_phrase('a', 'a'))

    def test_true_multi_char(self):
        self.assertTrue(generate_phrase('abc', 'bca'))

    def test_true_dif_lengths(self):
        self.assertTrue(generate_phrase('abc', 'bcabcaca'))

    def test_true_mixed_case(self):
        self.assertTrue(generate_phrase('AbC', 'bcAbcaCa'))

    def test_true_special_chars(self):
        self.assertTrue(
            generate_phrase('* A £ b % C !', 'b !! c% $  £Abc* aCa'))

    def test_true_more_complex_case(self):
        self.assertTrue(
            generate_phrase('Robyn Seymour-Jones',
                            'euvoqJsn-bSmofje-roy neRJoy'))

    def test_true_empty_string(self):
        self.assertTrue(generate_phrase('', 'bug'))

    # False cases
    def test_false_single_char(self):
        self.assertFalse(generate_phrase('a', 'b'))

    def test_false_multi_char(self):
        self.assertFalse(generate_phrase('abc', 'bee'))

    def test_false_too_few_chars(self):
        self.assertFalse(generate_phrase('butterfly', 'butter'))

    def test_false_wrong_chars(self):
        self.assertFalse(generate_phrase('dragonfly', 'butterfly'))


if __name__ == '__main__':
    main()
    