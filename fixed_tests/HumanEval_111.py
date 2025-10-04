import unittest

class TestHistogram(unittest.TestCase):

    def test_empty_string(self):
        """Test with an empty input string."""
        self.assertDictEqual(histogram(''), {})

    def test_single_letter_no_spaces(self):
        """Test with a single letter (implicitly count 1).
        The problem implies space-separated, but if a single char, it would be 'a'.
        Let's assume 'a' translates to 'a' rather than 'a b c'.
        If it strictly means space-separated, 'a' might not be a valid input unless 'a b' is for 'a'.
        Given 'a b c' example, I'll interpret 'a' as a single letter string.
        However, the problem statement "space separated lowercase letters" implies at least two letters if we parse strictly 'a b'.
        Let's make this test case conform to "space separated" and have just one letter like 'a b' but it means 'a':1.
        No, the examples 'a b c' and 'a b b a' clearly separate letters by single spaces.
        A single character string 'a' would not be "space separated".
        Let's interpret `histogram('a')` as a special case where the 'a' is the only character.
        If `split()` is used, 'a'.split() -> ['a'].
        This seems reasonable.
        """
        self.assertDictEqual(histogram('a'), {'a': 1})

    def test_multiple_unique_letters_all_one_count(self):
        """Test with multiple unique letters, each occurring once."""
        self.assertDictEqual(histogram('a b c'), {'a': 1, 'b': 1, 'c': 1})

    def test_two_letters_same_max_count(self):
        """Test with two letters having the same maximum occurrence."""
        self.assertDictEqual(histogram('a b b a'), {'a': 2, 'b': 2})

    def test_multiple_letters_two_max_counts_with_others(self):
        """Test with multiple letters, where two have the max count and others have less."""
        self.assertDictEqual(histogram('a b c a b'), {'a': 2, 'b': 2})

    def test_single_letter_has_max_count(self):
        """Test where only one letter has the maximum occurrence."""
        self.assertDictEqual(histogram('b b b b a'), {'b': 4})

    def test_longer_string_one_clear_max(self):
        """Test a longer string where one letter clearly has the highest count."""
        # 'x': 3, 'y': 2, 'z': 1, 'w': 1
        self.assertDictEqual(histogram('x y z x y x w'), {'x': 3})

    def test_longer_string_multiple_max_counts(self):
        """Test a longer string where multiple letters share the highest count."""
        # 'p': 3, 'q': 3, 'r': 2, 's': 1
        expected = {'p': 3, 'q': 3}
        # The order of keys in a dictionary might not be guaranteed in older Python versions,
        # but for assertDictEqual, it compares content.
        self.assertDictEqual(histogram('p q r s p q r p q'), expected)

    def test_all_same_letter(self):
        """Test a string consisting of only one repeated letter."""
        self.assertDictEqual(histogram('c c c c c'), {'c': 5})

    def test_all_unique_letters_different_lengths_no_max(self):
        """Test a case with many unique letters, where each is a max of 1."""
        self.assertDictEqual(histogram('x y z w v u t s r q p o n m l k j i h g f e d'),
                             {'x':1, 'y':1, 'z':1, 'w':1, 'v':1, 'u':1, 't':1, 's':1, 'r':1, 'q':1, 'p':1, 'o':1, 'n':1, 'm':1, 'l':1, 'k':1, 'j':1, 'i':1, 'h':1, 'g':1, 'f':1, 'e':1, 'd':1})