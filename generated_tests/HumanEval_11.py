import unittest

# Assume the function 'string_xor' exists and is imported or defined elsewhere.
# For example:
# def string_xor(a: str, b: str) -> str:
#     result = []
#     # Assuming inputs are always of equal length based on typical binary XOR context and example
#     for i in range(len(a)):
#         if a[i] == b[i]:
#             result.append('0')
#         else:
#             result.append('1')
#     return "".join(result)

class TestStringXOR(unittest.TestCase):

    def test_single_bit_zero_xor_zero(self):
        self.assertEqual('0', string_xor('0', '0'))

    def test_single_bit_one_xor_one(self):
        self.assertEqual('0', string_xor('1', '1'))

    def test_single_bit_zero_xor_one(self):
        self.assertEqual('1', string_xor('0', '1'))

    def test_single_bit_one_xor_zero(self):
        self.assertEqual('1', string_xor('1', '0'))

    def test_example_case(self):
        self.assertEqual('100', string_xor('010', '110'))

    def test_all_zeros_xor_all_ones(self):
        self.assertEqual('11111', string_xor('00000', '11111'))

    def test_all_ones_xor_all_ones(self):
        self.assertEqual('00000', string_xor('11111', '11111'))

    def test_string_xor_with_itself(self):
        self.assertEqual('000000', string_xor('101010', '101010'))

    def test_long_alternating_patterns(self):
        self.assertEqual('11111111', string_xor('01010101', '10101010'))

    def test_another_long_mixed_case(self):
        self.assertEqual('1001100110', string_xor('1100110011', '0101010101'))
    def test_unequal_length_strings(self):
            """
            Test case for handling strings of unequal length, which should raise a ValueError.
            This specifically targets the 'raise ValueError' branch on line 18, ensuring
            it is covered.
            """
            with self.assertRaises(ValueError) as cm:
                string_xor("01", "101")
            self.assertEqual(str(cm.exception), "Input strings must be of equal length for XOR operation.")

            with self.assertRaises(ValueError) as cm:
                string_xor("101", "01")
            self.assertEqual(str(cm.exception), "Input strings must be of equal length for XOR operation.")

            with self.assertRaises(ValueError) as cm:
                string_xor("", "0")
            self.assertEqual(str(cm.exception), "Input strings must be of equal length for XOR operation.")

    def test_empty_strings(self):
            """
            Test case for XORing two empty strings.
            This covers the scenario where the loop is not entered and the final return
            statement (line 28) is executed with an empty result_chars list.
            """
            self.assertEqual(string_xor("", ""), "")

    def test_single_character_strings(self):
            """
            Additional test cases for single-character strings to ensure basic XOR logic
            for all four combinations is robustly covered.
            """
            self.assertEqual(string_xor("0", "0"), "0")
            self.assertEqual(string_xor("0", "1"), "1")
            self.assertEqual(string_xor("1", "0"), "1")
            self.assertEqual(string_xor("1", "1"), "0")

    def test_longer_alternating_strings(self):
            """
            Test case with longer strings where results are all '1's, ensuring loop and logic
            work for longer patterns.
            """
            self.assertEqual(string_xor("1010101010", "0101010101"), "1111111111")
            self.assertEqual(string_xor("00110011", "11001100"), "11111111")
