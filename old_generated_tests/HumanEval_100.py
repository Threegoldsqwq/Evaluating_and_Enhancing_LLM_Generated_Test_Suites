import unittest

class TestMakeAPile(unittest.TestCase):

    def test_n_is_1(self):
        # Smallest possible input (odd)
        self.assertEqual(make_a_pile(1), [1])

    def test_n_is_2(self):
        # Smallest even input
        self.assertEqual(make_a_pile(2), [2, 4])

    def test_n_is_3_example(self):
        # Given example in the problem description (odd)
        self.assertEqual(make_a_pile(3), [3, 5, 7])

    def test_n_is_4(self):
        # Another small even input
        self.assertEqual(make_a_pile(4), [4, 6, 8, 10])

    def test_n_is_5(self):
        # Medium odd input
        self.assertEqual(make_a_pile(5), [5, 7, 9, 11, 13])

    def test_n_is_6(self):
        # Medium even input
        self.assertEqual(make_a_pile(6), [6, 8, 10, 12, 14, 16])

    def test_n_is_7(self):
        # Another medium odd input
        self.assertEqual(make_a_pile(7), [7, 9, 11, 13, 15, 17, 19])

    def test_n_is_8(self):
        # Another medium even input
        self.assertEqual(make_a_pile(8), [8, 10, 12, 14, 16, 18, 20, 22])

    def test_n_is_10(self):
        # Larger even input
        self.assertEqual(make_a_pile(10), [10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_n_is_15(self):
        # Larger odd input
        self.assertEqual(make_a_pile(15), [15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43])

# This allows running the tests directly if the file is executed.
# In a real scenario, `make_a_pile` function would be defined or imported.
if __name__ == '__main__':
    # Placeholder for the function for testing purposes.
    # In a real test setup, you would import the actual function.
    def make_a_pile(n: int) -> list[int]:
        pile = []
        current_stones = n
        for _ in range(n):
            pile.append(current_stones)
            current_stones += 2
        return pile

    unittest.main()