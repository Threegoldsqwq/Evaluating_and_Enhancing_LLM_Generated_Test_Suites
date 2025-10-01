import unittest

# Assume the function to be tested is named 'count_prime_hex_digits'
# and is available in the scope or imported.

class TestCountPrimeHexDigits(unittest.TestCase):

    def test_empty_string(self):
        # Test with an empty string, should return 0
        self.assertEqual(count_prime_hex_digits(""), 0)

    def test_no_prime_digits(self):
        # Test with a string containing only non-prime hexadecimal digits
        self.assertEqual(count_prime_hex_digits("01468ACEF"), 0)

    def test_all_prime_digits(self):
        # Test with a string containing all prime hexadecimal digits
        self.assertEqual(count_prime_hex_digits("2357BD"), 6)

    def test_example_ab(self):
        # Example 1 from the problem description: "AB"
        self.assertEqual(count_prime_hex_digits("AB"), 1) # B (11) is prime

    def test_example_1077e(self):
        # Example 2 from the problem description: "1077E"
        self.assertEqual(count_prime_hex_digits("1077E"), 2) # Two '7's are prime

    def test_example_abed1a33(self):
        # Example 3 from the problem description: "ABED1A33"
        self.assertEqual(count_prime_hex_digits("ABED1A33"), 4) # B, D, 3, 3 are prime

    def test_example_all_digits_mix(self):
        # Example 4 from the problem description: "123456789ABCDEF0"
        self.assertEqual(count_prime_hex_digits("123456789ABCDEF0"), 6) # 2, 3, 5, 7, B, D are prime

    def test_example_2020(self):
        # Example 5 from the problem description: "2020"
        self.assertEqual(count_prime_hex_digits("2020"), 2) # Two '2's are prime

    def test_single_prime_digit_in_long_string(self):
        # Test with a string containing only one prime digit amidst many non-primes
        self.assertEqual(count_prime_hex_digits("01468ACEF01468ACEF01468ACEFB"), 1) # Only B is prime

    def test_mixed_long_string_with_duplicates(self):
        # Test with a longer, more complex string containing various prime and non-prime digits
        self.assertEqual(count_prime_hex_digits("DEADBEEFCAFEDECADE"), 5) 
        # Primes: D (13), D (13), B (11), D (13), D (13) = 5