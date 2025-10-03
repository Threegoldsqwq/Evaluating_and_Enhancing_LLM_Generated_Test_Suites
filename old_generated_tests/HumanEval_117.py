import unittest

# Assume the select_words function is defined elsewhere, e.g.:
# def select_words(s: str, n: int) -> list[str]:
#     vowels = "aeiouAEIOU"
#     consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
#
#     if not s:
#         return []
#
#     result = []
#     words = s.split()
#
#     for word in words:
#         consonant_count = 0
#         for char in word:
#             if char.isalpha() and char not in vowels:
#                 consonant_count += 1
#         if consonant_count == n:
#             result.append(word)
#     return result


class TestSelectWords(unittest.TestCase):

    def test_single_match_from_example(self):
        # Test case from problem description: single word matching
        self.assertEqual(select_words("Mary had a little lamb", 4), ["little"])

    def test_multiple_matches_from_example(self):
        # Test case from problem description: multiple words matching
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])

    def test_no_matches_found(self):
        # Test case from problem description: no words match the criteria
        self.assertEqual(select_words("simple white space", 2), [])

    def test_empty_string(self):
        # Test case for an empty input string
        self.assertEqual(select_words("", 5), [])

    def test_n_is_zero_with_vowel_only_words(self):
        # Test for n=0, expecting words with no consonants (e.g., single vowels)
        # 'a', 'I', 'O', 'U' have 0 consonants. 'an' has 1.
        self.assertEqual(select_words("a an I O U", 0), ["a", "I", "O", "U"])

    def test_mixed_case_and_multiple_matches_different_positions(self):
        # Test with mixed case words and multiple matches at various positions
        # "Jump": J,m,p (3)
        # "Walk": W,l,k (3)
        # "Sing": S,n,g (3)
        self.assertEqual(select_words("Jump and Walk and Sing and Run", 3), ["Jump", "Walk", "Sing"])

    def test_single_word_in_string_that_matches(self):
        # Test with a string containing only one word, which matches the criteria
        # "Programming": P,r,g,r,m,m,n,g (8)
        self.assertEqual(select_words("Programming", 8), ["Programming"])

    def test_string_with_only_spaces(self):
        # Test with a string composed solely of spaces, should result in an empty list
        self.assertEqual(select_words("   ", 1), [])

    def test_n_larger_than_any_possible_consonant_count(self):
        # Test when 'n' is unrealistically large, ensuring no matches are found
        # "apple": p,p,l (3)
        # "banana": b,n,n (3)
        # "orange": r,n,g (3)
        self.assertEqual(select_words("apple banana orange", 10), [])

    def test_leading_trailing_and_multiple_spaces_with_match(self):
        # Test handling of leading, trailing, and multiple spaces between words
        # "Hello": H,l,l (3)
        # "world": w,r,l,d (4)
        self.assertEqual(select_words("  Hello   world  ", 4), ["world"])