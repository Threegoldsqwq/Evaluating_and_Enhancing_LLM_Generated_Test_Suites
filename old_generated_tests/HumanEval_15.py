import unittest

# Assume the function string_sequence(n) exists and is imported or defined elsewhere.
# For example:
# def string_sequence(n):
#     return ' '.join(str(i) for i in range(n + 1))

class TestStringSequence(unittest.TestCase):

    def test_zero(self):
        """Test with n = 0, should return '0'."""
        self.assertEqual(string_sequence(0), '0')

    def test_one(self):
        """Test with n = 1, should return '0 1'."""
        self.assertEqual(string_sequence(1), '0 1')

    def test_small_positive(self):
        """Test with a small positive n like 3."""
        self.assertEqual(string_sequence(3), '0 1 2 3')

    def test_example_five(self):
        """Test with the example n = 5."""
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

    def test_ten(self):
        """Test with n = 10, covering single and double-digit numbers."""
        self.assertEqual(string_sequence(10), '0 1 2 3 4 5 6 7 8 9 10')

    def test_larger_positive(self):
        """Test with a larger positive n like 15."""
        self.assertEqual(string_sequence(15), '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15')

    def test_single_digit_max(self):
        """Test with n = 9, the largest single-digit number."""
        self.assertEqual(string_sequence(9), '0 1 2 3 4 5 6 7 8 9')

    def test_two_digit_start(self):
        """Test with n = 11, ensuring correct two-digit numbers."""
        self.assertEqual(string_sequence(11), '0 1 2 3 4 5 6 7 8 9 10 11')

    def test_moderate_positive(self):
        """Test with a moderately sized positive n like 7."""
        self.assertEqual(string_sequence(7), '0 1 2 3 4 5 6 7')

    def test_twenty(self):
        """Test with n = 20, a slightly larger case."""
        expected_output = '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20'
        self.assertEqual(string_sequence(20), expected_output)