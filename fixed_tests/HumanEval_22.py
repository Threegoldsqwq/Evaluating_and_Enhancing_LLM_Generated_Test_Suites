import unittest

class TestFilterIntegers(unittest.TestCase):

    def test_empty_list(self):
        # Test with an empty list
        self.assertEqual(filter_integers([]), [])

    def test_only_integers(self):
        # Test with a list containing only integers
        self.assertEqual(filter_integers([1, 2, 3, 42, -5]), [1, 2, 3, 42, -5])

    def test_no_integers(self):
        # Test with a list containing no integers
        self.assertEqual(filter_integers(['a', 3.14, {}, [], None]), [])

    def test_mixed_types_basic(self):
        # Test with a basic mix of integers and other types (from example 1)
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])

    def test_mixed_types_complex(self):
        # Test with a more complex mix including various non-integer types
        self.assertEqual(filter_integers([1, 'abc', 2.5, True, None, {'key': 'value'}, [4, 5], 100, False]), [1, True, 100, False])

    def test_booleans_as_integers(self):
        # Test specifically for boolean values, which are instances of int in Python
        self.assertEqual(filter_integers([True, False, 0, 1]), [True, False, 0, 1])

    def test_floats_with_integer_values(self):
        # Test that floats, even if they have integer values, are not included
        self.assertEqual(filter_integers([1.0, 2.0, 3.14, -5.0, 7]), [7])

    def test_negative_and_zero_integers(self):
        # Test with negative integers and zero
        self.assertEqual(filter_integers([-1, 0, -100, 'abc', 5]), [-1, 0, -100, 5])

    def test_duplicate_integers(self):
        # Test with duplicate integers and mixed types
        self.assertEqual(filter_integers([1, 2, 1, 'a', 3, 2.0, 2, True]), [1, 2, 1, 3, 2, True])

    def test_large_integers(self):
        # Test with very large integers
        self.assertEqual(filter_integers([10**100, 'small', -10**50, 0.5, 999999999999999]), [10**100, -10**50, 999999999999999])

# Note: The 'filter_integers' function is assumed to exist for these tests to run.
# For example, a basic implementation could be:
# def filter_integers(values):
#     return [value for value in values if isinstance(value, int)]