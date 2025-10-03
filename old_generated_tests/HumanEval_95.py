import unittest

class TestCheckDictCase(unittest.TestCase):

    def test_all_lowercase_keys(self):
        # All keys are lowercase strings. Should return True.
        self.assertTrue(check_dict_case({"a":"apple", "b":"banana", "c":"cherry"}))

    def test_all_uppercase_keys(self):
        # All keys are uppercase strings. Should return True.
        self.assertTrue(check_dict_case({"STATE":"NC", "ZIP":"12345", "COUNTRY":"USA"}))

    def test_empty_dictionary(self):
        # Empty dictionary. Should return False.
        self.assertFalse(check_dict_case({}))

    def test_mixed_case_keys_lowercase_and_uppercase(self):
        # Keys are a mix of lowercase and uppercase strings. Should return False.
        self.assertFalse(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))

    def test_mixed_case_keys_with_title_or_capitalized(self):
        # Keys contain strings that are neither all lowercase nor all uppercase. Should return False.
        self.assertFalse(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))

    def test_contains_non_string_integer_key(self):
        # Contains a non-string key (integer). Should return False.
        self.assertFalse(check_dict_case({"a":"apple", 8:"banana", "c":"carrot"}))

    def test_contains_non_string_float_key(self):
        # Contains a non-string key (float). Should return False.
        self.assertFalse(check_dict_case({"key1":1, 3.14:"pi", "key2":2}))

    def test_single_lowercase_key(self):
        # Single key, which is lowercase. Should return True.
        self.assertTrue(check_dict_case({"singlekey":"value"}))

    def test_single_uppercase_key(self):
        # Single key, which is uppercase. Should return True.
        self.assertTrue(check_dict_case({"SINGLEKEY":"value"}))

    def test_keys_with_mixed_internal_casing(self):
        # Keys are strings but contain both lower and upper case characters, not purely one or the other. Should return False.
        self.assertFalse(check_dict_case({"myKey":"value1", "anotherKey":"value2"}))