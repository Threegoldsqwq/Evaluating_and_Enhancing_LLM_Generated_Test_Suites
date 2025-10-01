import unittest

# Assume the 'bf' function is defined elsewhere, e.g., in a file named 'solution.py'
# from solution import bf 

class TestBetweenPlanets(unittest.TestCase):

    def test_standard_range_forward_order(self):
        """
        Tests a standard case with planets provided in increasing order of distance from the Sun.
        """
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))

    def test_standard_range_reverse_input_order(self):
        """
        Tests a standard case with planets provided in decreasing order of distance from the Sun.
        The output should still be sorted by proximity to the Sun.
        """
        self.assertEqual(bf("Earth", "Mercury"), ("Venus",))

    def test_large_range_forward_order(self):
        """
        Tests a larger range of planets, from closer to the Sun to further.
        """
        self.assertEqual(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))

    def test_single_planet_between_forward_input(self):
        """
        Tests a case where exactly one planet is between the two given planets, forward input order.
        """
        self.assertEqual(bf("Venus", "Mars"), ("Earth",))

    def test_single_planet_between_reverse_input(self):
        """
        Tests a case where exactly one planet is between the two given planets, reverse input order.
        """
        self.assertEqual(bf("Mars", "Venus"), ("Earth",))
        
    def test_adjacent_planets_forward_input(self):
        """
        Tests when the two input planets are adjacent and provided in forward order.
        Should return an empty tuple as there are no planets *between* them.
        """
        self.assertEqual(bf("Mercury", "Venus"), ())

    def test_adjacent_planets_reverse_input(self):
        """
        Tests when the two input planets are adjacent and provided in reverse order.
        Should return an empty tuple.
        """
        self.assertEqual(bf("Neptune", "Uranus"), ())

    def test_same_planet_input(self):
        """
        Tests when both input planet names are the same.
        Should return an empty tuple.
        """
        self.assertEqual(bf("Earth", "Earth"), ())

    def test_one_invalid_planet_name(self):
        """
        Tests when one of the input planet names is not a valid planet.
        Should return an empty tuple.
        """
        self.assertEqual(bf("Pluto", "Jupiter"), ())

    def test_both_invalid_planet_names(self):
        """
        Tests when both input planet names are not valid.
        Should return an empty tuple.
        """
        self.assertEqual(bf("Krypton", "Vulcan"), ())

# To run these tests, you would typically use:
# if __name__ == '__main__':
#     unittest.main()