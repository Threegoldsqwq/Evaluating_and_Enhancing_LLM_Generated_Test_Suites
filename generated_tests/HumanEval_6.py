import unittest

# Assume parse_nested_parens function exists elsewhere and is imported or defined.
# For the purpose of running these tests, you might define a dummy function like:
# def parse_nested_parens(s: str) -> list[int]:
#     # Dummy implementation to allow tests to run without the actual function
#     if not s.strip():
#         return []
#     groups = s.split(' ')
#     results = []
#     for group in groups:
#         if not group: # Handle cases like '()' '  (())' resulting in an empty string from split
#             continue
#         max_level = 0
#         current_level = 0
#         for char in group:
#             if char == '(':
#                 current_level += 1
#                 max_level = max(max_level, current_level)
#             elif char == ')':
#                 current_level -= 1
#         results.append(max_level)
#     return results


class TestParseNestedParens(unittest.TestCase):

    def test_single_group_level_1(self):
        """Test with a single group having one level of nesting."""
        self.assertEqual(parse_nested_parens('()'), [1])

    def test_single_group_level_2(self):
        """Test with a single group having two levels of nesting."""
        self.assertEqual(parse_nested_parens('(())'), [2])

    def test_single_group_level_3(self):
        """Test with a single group having three levels of nesting."""
        self.assertEqual(parse_nested_parens('((()))'), [3])

    def test_multiple_simple_groups(self):
        """Test with multiple groups, each having simple, distinct nesting levels."""
        self.assertEqual(parse_nested_parens('() (()) ((()))'), [1, 2, 3])

    def test_example_from_problem_description(self):
        """Test the exact example provided in the problem description."""
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

    def test_empty_input_string(self):
        """Test with an empty input string, expecting an empty list."""
        self.assertEqual(parse_nested_parens(''), [])

    def test_input_string_with_only_spaces(self):
        """Test with an input string containing only spaces, expecting an empty list."""
        self.assertEqual(parse_nested_parens('   '), [])

    def test_multiple_groups_same_level(self):
        """Test with multiple groups that all have the same simple nesting level."""
        self.assertEqual(parse_nested_parens('() () ()'), [1, 1, 1])

    def test_very_deep_nesting_in_one_group(self):
        """Test a single group with an exceptionally deep level of nesting."""
        self.assertEqual(parse_nested_parens('((((((()))))))'), [6])

    def test_complex_mix_of_deep_and_wide_groups(self):
        """Test a complex scenario with a mix of deep, wide, and varied nesting structures."""
        # ( () () ) -> 2
        # ( ( ( () ) ) () ) -> 4
        # () () -> 1 (assuming parse handles multiple top-level groups separately for the max of the whole string)
        # ( () ) -> 2
        self.assertEqual(parse_nested_parens('(()()()) (((()))()) ()() (())'), [2, 4, 1, 2])