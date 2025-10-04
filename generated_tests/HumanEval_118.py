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

    def test_empty_string(self):
            # Covers the case where len(word) < 3, preventing the main loop from executing.
            self.assertEqual(get_closest_vowel(""), "")

    def test_short_strings_no_loop(self):
            # Covers cases where len(word) < 3 (length 1 and 2), preventing the main loop from executing.
            self.assertEqual(get_closest_vowel("a"), "")
            self.assertEqual(get_closest_vowel("b"), "")
            self.assertEqual(get_closest_vowel("ae"), "")
            self.assertEqual(get_closest_vowel("ba"), "")
            self.assertEqual(get_closest_vowel("bb"), "")

    def test_no_vowels_in_word(self):
            # Covers words containing no English vowels, ensuring the loop completes and returns empty string.
            self.assertEqual(get_closest_vowel("rhythm"), "")
            self.assertEqual(get_closest_vowel("fly"), "")
            self.assertEqual(get_closest_vowel("crypts"), "")

    def test_vowels_at_boundaries_only(self):
            # Vowels are present, but only at the beginning or end, or such that they are not between consonants.
            # These cases prevent the inner conditions from being met.
            self.assertEqual(get_closest_vowel("apple"), "") # 'a' at start, 'e' at end
            self.assertEqual(get_closest_vowel("idea"), "")  # 'i' at start, 'a' at end
            self.assertEqual(get_closest_vowel("aeiou"), "") # Vowels are always next to other vowels
            self.assertEqual(get_closest_vowel("coala"), "") # 'o' is between 'c' and 'a' (vowel), 'a' is between 'o' (vowel) and 'l'

    def test_vowel_at_smallest_valid_index(self):
            # Tests when the closest vowel from the right is at the smallest possible index (i=1).
            self.assertEqual(get_closest_vowel("bab"), "a")
            self.assertEqual(get_closest_vowel("xey"), "e")
            self.assertEqual(get_closest_vowel("fic"), "i")

    def test_vowel_at_largest_valid_index(self):
            # Tests when the closest vowel from the right is at the largest possible index (len(word)-2).
            self.assertEqual(get_closest_vowel("cabac"), "a") # 'a' at index 3 (len-2) between 'b' and 'c'
            self.assertEqual(get_closest_vowel("opener"), "e") # 'e' at index 4 (len-2) between 'n' and 'r'

    def test_multiple_valid_vowels_rightmost_priority(self):
            # Ensures that the function correctly picks the rightmost valid vowel.
            self.assertEqual(get_closest_vowel("banana"), "a") # 'a' at index 4 ('n'a'n') should be chosen over 'a' at index 2
            self.assertEqual(get_closest_vowel("catamaran"), "a") # 'a' at index 7 ('r'a'n') over 'a' at index 5 ('m'a'r')
            self.assertEqual(get_closest_vowel("celebration"), "a") # 'a' at index 7 ('r'a't') over 'e' at index 2 ('c'e'l') or 'i' at index 5 ('b'i'l')

    def test_case_sensitivity_vowels_and_consonants(self):
            # Tests with a mix of uppercase and lowercase characters.
            self.assertEqual(get_closest_vowel("bAc"), "A")
            self.assertEqual(get_closest_vowel("BYAYZ"), "A")
            self.assertEqual(get_closest_vowel("bAnAnA"), "A")
            self.assertEqual(get_closest_vowel("sChOOl"), "") # 'O' at index 3 is between 'h' and 'O' (vowel), so no match.

    def test_complex_words_no_match(self):
            # Words where the loop runs extensively but no valid vowel is found.
            self.assertEqual(get_closest_vowel("aquarium"), "") # All vowels either at boundary or next to other vowels
            self.assertEqual(get_closest_vowel("scrooge"), "") # Vowels are 'o', 'o', 'o', 'e'. 'o' at 3 between 'r' and 'o' (vowel).
if __name__ == '__main__':
    unittest.main()