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

    def test_bf_invalid_planet_names(self):
            """
            Tests scenarios where one or both input planet names are not valid.
            This covers the 'True' branch of the first 'if' condition:
            'if planet1 not in PLANETS or planet2 not in PLANETS:'
            """
            # Test case: first planet invalid, second valid
            self.assertEqual(bf("Pluto", "Earth"), ())
            # Test case: first planet valid, second invalid
            self.assertEqual(bf("Earth", "Krypton"), ())
            # Test case: both planets invalid
            self.assertEqual(bf("X", "Y"), ())
            # Test case: case sensitivity (name must match exactly)
            self.assertEqual(bf("mercury", "Venus"), ())
            self.assertEqual(bf("Mercury", "venus"), ())
            self.assertEqual(bf("earth", "Mars"), ())

    def test_bf_no_planets_in_between(self):
            """
            Tests scenarios where there are no planets strictly between the two
            given planets (either the same planet or adjacent planets).
            This covers the 'True' branch of the second 'if' condition:
            'if end_slice_index - start_slice_index <= 1:'
            """
            # Test case: same planet
            self.assertEqual(bf("Earth", "Earth"), ())
            # Test case: adjacent planets (forward order)
            self.assertEqual(bf("Mercury", "Venus"), ())
            self.assertEqual(bf("Venus", "Earth"), ())
            self.assertEqual(bf("Uranus", "Neptune"), ())
            # Test case: adjacent planets (reverse order)
            self.assertEqual(bf("Venus", "Mercury"), ())
            self.assertEqual(bf("Neptune", "Uranus"), ())

    def test_bf_valid_planets_various_ranges(self):
            """
            Tests various valid planet combinations, ensuring correct slicing
            and handling of different ranges and orders.
            This helps ensure the 'False' branches of the 'if' conditions
            and the slicing logic are fully covered for various inputs.
            """
            # Standard case, forward order
            self.assertEqual(bf("Mercury", "Mars"), ("Venus", "Earth"))
            # Standard case, reverse order
            self.assertEqual(bf("Mars", "Mercury"), ("Earth", "Venus"))
            # Larger range, forward order
            self.assertEqual(bf("Earth", "Neptune"), ("Mars", "Jupiter", "Saturn", "Uranus"))
            # Larger range, reverse order
            self.assertEqual(bf("Neptune", "Earth"), ("Uranus", "Saturn", "Jupiter", "Mars"))
            # Full range, forward order
            self.assertEqual(bf("Mercury", "Neptune"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"))
            # Full range, reverse order
            self.assertEqual(bf("Neptune", "Mercury"), ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus"))
            # Case with exactly one planet in between
            self.assertEqual(bf("Mercury", "Earth"), ("Venus",))
            self.assertEqual(bf("Earth", "Mercury"), ("Venus",))
# To run these tests, you would typically use:
# if __name__ == '__main__':
#     unittest.main()