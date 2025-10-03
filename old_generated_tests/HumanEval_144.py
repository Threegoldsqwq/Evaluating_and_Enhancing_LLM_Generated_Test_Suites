import unittest

# Assume the 'simplify' function is defined elsewhere, for example:
# from your_module import simplify

class TestSimplify(unittest.TestCase):

    def test_example_one_product_is_one(self):
        # Product: (1/5) * (5/1) = 5/5 = 1 (a whole number)
        self.assertTrue(simplify("1/5", "5/1"))

    def test_example_two_product_is_fraction(self):
        # Product: (1/6) * (2/1) = 2/6 = 1/3 (not a whole number)
        self.assertFalse(simplify("1/6", "2/1"))

    def test_example_three_product_is_improper_fraction(self):
        # Product: (7/10) * (10/2) = 70/20 = 7/2 = 3.5 (not a whole number)
        self.assertFalse(simplify("7/10", "10/2"))

    def test_product_is_a_different_whole_number(self):
        # Product: (1/3) * (9/1) = 9/3 = 3 (a whole number)
        self.assertTrue(simplify("1/3", "9/1"))

    def test_product_involving_cancellation_not_a_whole_number(self):
        # Product: (3/8) * (2/5) = 6/40 = 3/20 (not a whole number)
        self.assertFalse(simplify("3/8", "2/5"))

    def test_product_of_improper_fractions_is_whole(self):
        # Product: (10/3) * (3/5) = 30/15 = 2 (a whole number)
        self.assertTrue(simplify("10/3", "3/5"))

    def test_product_of_improper_fractions_is_not_whole(self):
        # Product: (7/4) * (5/2) = 35/8 (not a whole number)
        self.assertFalse(simplify("7/4", "5/2"))

    def test_large_numbers_that_simplify_to_a_whole_number(self):
        # Product: (120/7) * (14/30) = 1680/210 = 8 (a whole number)
        self.assertTrue(simplify("120/7", "14/30"))

    def test_large_numbers_that_do_not_simplify_to_a_whole_number(self):
        # Product: (99/10) * (2/3) = 198/30 = 33/5 = 6.6 (not a whole number)
        self.assertFalse(simplify("99/10", "2/3"))

    def test_product_results_in_another_simple_whole_number(self):
        # Product: (5/2) * (8/1) = 40/2 = 20 (a whole number)
        self.assertTrue(simplify("5/2", "8/1"))