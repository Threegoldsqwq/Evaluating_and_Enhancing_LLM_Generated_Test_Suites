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