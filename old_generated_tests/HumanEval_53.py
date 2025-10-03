import unittest

# Assume the 'add' function exists in the global scope or can be imported.
# For demonstration purposes, if you were to run this file directly,
# you might temporarily define a placeholder:
# def add(x, y):
#     return x + y

class TestAddFunction(unittest.TestCase):

    def test_add_positive_integers_basic_1(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_positive_integers_basic_2(self):
        self.assertEqual(add(5, 7), 12)

    def test_add_with_zero_first(self):
        self.assertEqual(add(0, 10), 10)

    def test_add_with_zero_second(self):
        self.assertEqual(add(15, 0), 15)

    def test_add_two_negative_integers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_positive_and_negative_result_positive(self):
        self.assertEqual(add(10, -3), 7)

    def test_add_positive_and_negative_result_negative(self):
        self.assertEqual(add(3, -10), -7)

    def test_add_positive_and_negative_result_zero(self):
        self.assertEqual(add(5, -5), 0)

    def test_add_floating_point_numbers(self):
        self.assertEqual(add(2.5, 3.5), 6.0)

    def test_add_large_integers(self):
        self.assertEqual(add(1000000, 2000000), 3000000)

if __name__ == '__main__':
    # Placeholder for the add function for local execution/testing of test cases
    # In a real scenario, this function would be imported or defined elsewhere.
    def add(x, y):
        return x + y

    unittest.main()