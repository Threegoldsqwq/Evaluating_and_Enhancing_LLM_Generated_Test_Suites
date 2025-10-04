import unittest

class TestEncodeString(unittest.TestCase):
    """
    Test cases for a function that encodes a string by cycling groups of three characters.
    Assumes the cycling logic for a group 'abc' is 'bca'.
    Partial groups at the end (1 or 2 characters) are assumed to remain unchanged.
    """

    def test_empty_string(self):
        """Test with an empty string."""
        self.assertEqual(encode_cyclic(""), "")

    def test_single_character_string(self):
        """Test with a string of length 1 (partial group)."""
        self.assertEqual(encode_cyclic("a"), "a")

    def test_two_character_string(self):
            """Test with a string of length 2 (partial group)."""
            self.assertEqual(encode_cyclic("ab"), "ba")
    def test_three_character_string(self):
        """Test with a string of length 3 (single full group)."""
        self.assertEqual(encode_cyclic("abc"), "bca")

    def test_four_character_string(self):
        """Test with a string of length 4 (one full group + one partial)."""
        # abc -> bca, d -> d
        self.assertEqual(encode_cyclic("abcd"), "bcad")

    def test_five_character_string(self):
            """Test with a string of length 5 (one full group + two partial)."""
            # For "abcde":
            # "abc" -> "bca" (rotation left by 1)
            # "de"  -> "ed"  (rotation left by 1, 'd' moves to end, 'e' moves to front)
            # Expected result: "bca" + "ed" = "bcaed"
            self.assertEqual(encode_cyclic("abcde"), "bcaed")
    def test_six_character_string(self):
        """Test with a string of length 6 (two full groups)."""
        # abc -> bca, def -> efd
        self.assertEqual(encode_cyclic("abcdef"), "bcaefd")

    def test_longer_mixed_string(self):
        """Test with a longer string containing numbers and symbols."""
        # 123 -> 231, ABC -> BCA, xyz -> yzx, !@# -> @#!
        self.assertEqual(encode_cyclic("123ABCxyz!@#"), "231BCAyzx@#!")

    def test_string_with_spaces_and_repetition(self):
            """Test with a string containing spaces and repeated characters."""
            # Input: "   xyz   123" (length 12)
            # Groups: "   ", "xyz", "   ", "123"
            # Rotation:
            # "   " -> "   " (space is rotated to itself)
            # "xyz" -> "yzx"
            # "   " -> "   "
            # "123" -> "231"
            # Expected output: "   yzx   231"
            self.assertEqual(encode_cyclic("   xyz   123"), "   yzx   231")
    def test_string_all_same_characters(self):
        """Test with a string where all characters are identical."""
        # aaa -> aaa, aaa -> aaa, a -> a
        self.assertEqual(encode_cyclic("aaaaaaa"), "aaaaaaa")

    def test_decode_cyclic_empty_string(self):
            """Test decoding an empty string, covering the 'if chunk' condition false path."""
            self.assertEqual(decode_cyclic(""), "")

    def test_decode_cyclic_single_char(self):
            """Test decoding a single character string (chunk length 1)."""
            self.assertEqual(decode_cyclic("a"), "a")
            self.assertEqual(decode_cyclic("Z"), "Z")

    def test_decode_cyclic_two_chars(self):
            """Test decoding a two-character string (chunk length 2)."""
            # Encoded "ab" -> "ba". Decoded "ba" -> "ab"
            self.assertEqual(decode_cyclic("ba"), "ab")
            self.assertEqual(decode_cyclic("YX"), "XY")

    def test_decode_cyclic_three_chars(self):
            """Test decoding a three-character string (chunk length 3)."""
            # Encoded "abc" -> "bca". Decoded "bca" -> "abc"
            self.assertEqual(decode_cyclic("bca"), "abc")
            self.assertEqual(decode_cyclic("CBA"), "ABC")

    def test_decode_cyclic_four_chars(self):
            """Test decoding a four-character string (one group of 3, one of 1)."""
            # Original "abcd" -> encode_cyclic("abcd") -> "bcad"
            # decode_cyclic("bcad") should be "abcd"
            self.assertEqual(decode_cyclic("bcad"), "abcd")
            self.assertEqual(decode_cyclic("YZXA"), "XYZA") # From encode_cyclic("XYZA") -> "YZXA"

    def test_decode_cyclic_five_chars(self):
            """Test decoding a five-character string (one group of 3, one of 2)."""
            # Original "abcde" -> encode_cyclic("abcde") -> "bcaed"
            # decode_cyclic("bcaed") should be "abcde"
            self.assertEqual(decode_cyclic("bcaed"), "abcde")
            self.assertEqual(decode_cyclic("VWUXY"), "UVWXY") # From encode_cyclic("UVWXY") -> "VWUXY"

    def test_decode_cyclic_six_chars(self):
            """Test decoding a six-character string (two groups of 3)."""
            # Original "abcdef" -> encode_cyclic("abcdef") -> "bcaefd"
            # decode_cyclic("bcaefd") should be "abcdef"
            self.assertEqual(decode_cyclic("bcaefd"), "abcdef")
            self.assertEqual(decode_cyclic("231564"), "123456") # From encode_cyclic("123456") -> "231564"

    def test_decode_cyclic_long_strings(self):
            """Test decoding various longer strings to ensure full loop coverage."""
            long_string_1 = "TheQuickBrownFoxJumpsOverTheLazyDog" # Length 35, ends with 2-char chunk
            encoded_1 = encode_cyclic(long_string_1)
            self.assertEqual(decode_cyclic(encoded_1), long_string_1)

            long_string_2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" # Length 62, ends with 2-char chunk
            encoded_2 = encode_cyclic(long_string_2)
            self.assertEqual(decode_cyclic(encoded_2), long_string_2)

            long_string_3 = "abc123def456ghi789jkl0" # Length 22, ends with 1-char chunk (after three groups of 3 for the last "jkl0")
            encoded_3 = encode_cyclic(long_string_3)
            self.assertEqual(decode_cyclic(encoded_3), long_string_3)

    def test_encode_decode_roundtrip_various_lengths(self):
            """Test encode and then decode across a range of string lengths to ensure integrity."""
            test_strings = [
                "",          # Length 0
                "a",         # Length 1
                "ab",        # Length 2
                "abc",       # Length 3
                "abcd",      # Length 4
                "abcde",     # Length 5
                "abcdef",    # Length 6
                "test",
                "hello world",
                "python programming",
                "1234567890",
                "!@#$%^&*()_+"
            ]
            for s in test_strings:
                encoded = encode_cyclic(s)
                decoded = decode_cyclic(encoded)
                self.assertEqual(decoded, s, f"Roundtrip failed for original string: '{s}'")
                # Also test for non-ascii characters for robustness (though not explicitly required by problem, good for general coverage)
                s_unicode = "你好世界" # Length 4, 3+1
                encoded_unicode = encode_cyclic(s_unicode)
                decoded_unicode = decode_cyclic(encoded_unicode)
                self.assertEqual(decoded_unicode, s_unicode, f"Roundtrip failed for original string: '{s_unicode}'")

        # Adding more specific encode_cyclic tests if line 1 (function def) was truly uncovered due to lack of diverse calls

    def test_encode_cyclic_empty_string_explicit(self):
            self.assertEqual(encode_cyclic(""), "")

    def test_encode_cyclic_single_char_explicit(self):
            self.assertEqual(encode_cyclic("x"), "x")

    def test_encode_cyclic_two_chars_explicit(self):
            self.assertEqual(encode_cyclic("yz"), "zy")

    def test_encode_cyclic_three_chars_explicit(self):
            self.assertEqual(encode_cyclic("stu"), "tus")

    def test_encode_cyclic_four_chars_explicit(self):
            self.assertEqual(encode_cyclic("wxyz"), "xwyz") # wxy -> xwy, then z

    def test_encode_cyclic_long_with_spaces_and_numbers(self):
            self.assertEqual(encode_cyclic("Hello Python 123"), "ellHooPytnh 123") # "Hel"->ellH, "lo "->o l, "Pyt"->ytP, "hon"->onh, " 12"->12 , "3"->3
            # Let's double check this manually:
            # "Hel" -> "elH"
            # "lo " -> "o l"
            # "Pyt" -> "ytP"
            # "hon" -> "onh"
            # " 12" -> "12 "
            # "3"   -> "3"
            # Combined: "elHo lytPonh12 3"
            self.assertEqual(encode_cyclic("Hello Python 123"), "elHo lytPonh12 3")
# If you want to run these tests directly, uncomment the following block:
# if __name__ == '__main__':
#     # Dummy encode function for testing purposes, replace with actual one
#     def encode(s: str) -> str:
#         encoded_parts = []
#         for i in range(0, len(s), 3):
#             chunk = s[i:i+3]
#             if len(chunk) == 3:
#                 encoded_parts.append(chunk[1] + chunk[2] + chunk[0])
#             else:
#                 encoded_parts.append(chunk)
#         return "".join(encoded_parts)
#
#     unittest.main(argv=['first-arg-is-ignored'], exit=False)