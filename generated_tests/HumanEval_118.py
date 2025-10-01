import unittest

# Assume the function 'get_closest_vowel' is defined elsewhere, for example:
# def get_closest_vowel(word: str) -> str:
#     vowels = "aeiouAEIOU"
#     
#     def is_vowel(char):
#         return char in vowels
#     
#     def is_consonant(char):
#         return char.isalpha() and not is_vowel(char)
#     
#     # Iterate from the second to the second-to-last character
#     # (indices 1 to len(word) - 2) from right to left
#     for i in range(len(word) - 2, 0, -1):
#         char = word[i]
#         if is_vowel(char):
#             # Check if it's surrounded by two consonants
#             if is_consonant(word[i-1]) and is_consonant(word[i+1]):
#                 return char
#     
#     return ""

class TestGetClosestVowel(unittest.TestCase):

    def test_example_yogurt(self):
        # Basic case from example: finds 'u'
        self.assertEqual(get_closest_vowel("yogurt"), "u")

    def test_example_full(self):
        # Basic case from example: finds 'U', case sensitive
        self.assertEqual(get_closest_vowel("FULL"), "U")

    def test_example_quick(self):
        # No vowel is surrounded by two consonants
        self.assertEqual(get_closest_vowel("quick"), "")

    def test_example_ab(self):
        # Word is too short to have a vowel surrounded by two consonants
        self.assertEqual(get_closest_vowel("ab"), "")

    def test_no_middle_vowel_apple(self):
        # Vowels 'a' and 'e' are at the edges, and 'i' isn't surrounded by consonants
        self.assertEqual(get_closest_vowel("apple"), "")

    def test_multiple_vowels_strength(self):
        # 'e' is the closest vowel from the right surrounded by consonants ('r' and 'n')
        self.assertEqual(get_closest_vowel("strength"), "e")

    def test_no_vowels(self):
        # Word contains no vowels at all
        self.assertEqual(get_closest_vowel("rhythm"), "")

    def test_short_word_with_match_cat(self):
        # A short word where the middle vowel 'a' is surrounded by 'c' and 't'
        self.assertEqual(get_closest_vowel("cat"), "a")

    def test_multiple_vowels_xylophone(self):
        # 'o' at index 6 (h O n) is found first from the right, before 'o' at index 3 (l O p)
        self.assertEqual(get_closest_vowel("xylophone"), "o")

    def test_multiple_vowels_beautiful(self):
        # 'u' is the rightmost vowel surrounded by consonants ('f' and 'l')
        self.assertEqual(get_closest_vowel("beautiful"), "u")

if __name__ == '__main__':
    unittest.main()