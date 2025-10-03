import unittest

class TestChangeBase(unittest.TestCase):

    def test_zero_x(self):
        # Test case: x is 0, should always return "0"
        self.assertEqual(change_base(0, 2), "0")
        self.assertEqual(change_base(0, 9), "0")

    def test_one_x(self):
        # Test case: x is 1, should always return "1"
        self.assertEqual(change_base(1, 2), "1")
        self.assertEqual(change_base(1, 7), "1")

    def test_docstring_example_one(self):
        # Test case from docstring: 8 in base 3
        self.assertEqual(change_base(8, 3), "22")

    def test_docstring_example_two(self):
        # Test case from docstring: 8 in base 2
        self.assertEqual(change_base(8, 2), "1000")

    def test_docstring_example_three(self):
        # Test case from docstring: 7 in base 2
        self.assertEqual(change_base(7, 2), "111")

    def test_power_of_base(self):
        # Test case: x is a power of the base
        self.assertEqual(change_base(9, 3), "100") # 3^2
        self.assertEqual(change_base(16, 2), "10000") # 2^4

    def test_one_less_than_power_of_base(self):
        # Test case: x is one less than a power of the base (all max digits)
        self.assertEqual(change_base(15, 2), "1111") # 2^4 - 1
        self.assertEqual(change_base(8, 9), "8") # 9^1 - 1

    def test_general_case_base_two(self):
        # Test case: A common number in binary
        self.assertEqual(change_base(13, 2), "1101")

    def test_max_base_value(self):
        # Test case: Using the maximum allowed base (9)
        self.assertEqual(change_base(26, 9), "28") # 2*9 + 8 = 26

    def test_larger_number_mixed_base(self):
        # Test case: A larger number with a non-binary, non-ternary base
        self.assertEqual(change_base(100, 4), "1210") # 1*4^3 + 2*4^2 + 1*4^1 + 0*4^0 = 64 + 32 + 4 + 0 = 100