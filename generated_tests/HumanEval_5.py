import unittest

class TestIntersperse(unittest.TestCase):

    def test_empty_list(self):
        # Test case: an empty list should remain empty
        self.assertEqual(intersperse([], 4), [])

    def test_single_element_list(self):
        # Test case: a list with a single element should remain unchanged
        self.assertEqual(intersperse([1], 4), [1])

    def test_two_elements_list(self):
        # Test case: two elements should have one delimiter between them
        self.assertEqual(intersperse([1, 2], 4), [1, 4, 2])

    def test_three_elements_list_example(self):
        # Test case: example from the problem description
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_list_with_duplicates(self):
        # Test case: list containing duplicate elements
        self.assertEqual(intersperse([5, 5, 5], 0), [5, 0, 5, 0, 5])

    def test_list_with_negative_numbers(self):
        # Test case: list containing negative numbers
        self.assertEqual(intersperse([-1, -2, -3], 99), [-1, 99, -2, 99, -3])

    def test_delimiter_is_an_element(self):
        # Test case: when the delimiter is also present as an element in the list
        self.assertEqual(intersperse([10, 20, 30], 10), [10, 10, 20, 10, 30])

    def test_list_with_zero_elements_and_negative_delimiter(self):
        # Test case: list with zero as an element and a negative delimiter
        self.assertEqual(intersperse([0, 1, 0, 2], -1), [0, -1, 1, -1, 0, -1, 2])

    def test_float_numbers(self):
        # Test case: list and delimiter containing float numbers
        self.assertEqual(intersperse([1.5, 2.5, 3.5], 0.5), [1.5, 0.5, 2.5, 0.5, 3.5])

    def test_longer_list(self):
        # Test case: a longer list to ensure it scales correctly
        self.assertEqual(
            intersperse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0),
            [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10]
        )

    def test_intersperse_with_none_delimiter(self):
            # Test with None as a delimiter
            numbers = [1, 2, 3]
            delimiter = None
            expected = [1, None, 2, None, 3]
            self.assertEqual(self.solution(numbers, delimiter), expected)

    def test_intersperse_with_float_delimiter(self):
            # Test with a float as a delimiter
            numbers = [10, 20]
            delimiter = 3.14
            expected = [10, 3.14, 20]
            self.assertEqual(self.solution(numbers, delimiter), expected)

    def test_intersperse_list_of_none(self):
            # Test with a list containing None values
            numbers = [None, None]
            delimiter = 'X'
            expected = [None, 'X', None]
            self.assertEqual(self.solution(numbers, delimiter), expected)

    def test_intersperse_list_of_floats(self):
            # Test with a list containing float values
            numbers = [1.1, 2.2, 3.3]
            delimiter = 0
            expected = [1.1, 0, 2.2, 0, 3.3]
            self.assertEqual(self.solution(numbers, delimiter), expected)

    def test_intersperse_list_of_mixed_types(self):
            # Test with a list containing mixed types and a boolean delimiter
            numbers = [1, 'two', 3.0, None, True]
            delimiter = False
            expected = [1, False, 'two', False, 3.0, False, None, False, True]
            self.assertEqual(self.solution(numbers, delimiter), expected)

    def test_intersperse_large_list(self):
            # Test with a large list to ensure correctness with many elements
            numbers = list(range(1000))
            delimiter = -1
            expected = []
            for i, num in enumerate(numbers):
                expected.append(num)
                if i < len(numbers) - 1:
                    expected.append(delimiter)
            self.assertEqual(self.solution(numbers, delimiter), expected)

    def test_intersperse_negative_and_zero_numbers(self):
            # Test with a list containing negative numbers and zero
            numbers = [-5, 0, 5]
            delimiter = 99
            expected = [-5, 99, 0, 99, 5]
            self.assertEqual(self.solution(numbers, delimiter), expected)
# Assuming the 'intersperse' function is defined elsewhere, for example:
# def intersperse(numbers, delimiter):
#     if not numbers:
#         return []
#     result = [numbers[0]]
#     for i in range(1, len(numbers)):
#         result.append(delimiter)
#         result.append(numbers[i])
#     return result

if __name__ == '__main__':
    # This is a placeholder for the actual function for local testing purposes.
    # In a real scenario, the 'intersperse' function would be imported.
    # def intersperse(numbers, delimiter):
    #     if not numbers:
    #         return []
    #     result = [numbers[0]]
    #     for i in range(1, len(numbers)):
    #         result.append(delimiter)
    #         result.append(numbers[i])
    #     return result

    unittest.main(argv=['first-arg-is-ignored'], exit=False)