import unittest

class TestDigitSum(unittest.TestCase):

    def test_empty_string(self):
        # Test case 1: Empty string should return 0
        self.assertEqual(digitSum(""), 0)

    def test_no_uppercase_characters(self):
        # Test case 2: String with only lowercase characters should return 0
        self.assertEqual(digitSum("abcdefg"), 0)

    def test_only_uppercase_characters(self):
        # Test case 3: String with only uppercase characters
        # A=65, B=66, C=67. Sum = 65+66+67 = 198
        self.assertEqual(digitSum("ABC"), 198)

    def test_mixed_case_example_1(self):
        # Test case 4: Example from problem description "abAB"
        # A=65, B=66. Sum = 65+66 = 131
        self.assertEqual(digitSum("abAB"), 131)

    def test_mixed_case_example_2(self):
        # Test case 5: Example from problem description "abcCd"
        # C=67. Sum = 67
        self.assertEqual(digitSum("abcCd"), 67)

    def test_mixed_case_example_3(self):
        # Test case 6: Example from problem description "helloE"
        # E=69. Sum = 69
        self.assertEqual(digitSum("helloE"), 69)

    def test_mixed_case_example_4(self):
        # Test case 7: Example from problem description "woArBld"
        # A=65, B=66. Sum = 65+66 = 131
        self.assertEqual(digitSum("woArBld"), 131)

    def test_mixed_case_example_5(self):
        # Test case 8: Example from problem description "aAaaaXa"
        # A=65, X=88. Sum = 65+88 = 153
        self.assertEqual(digitSum("aAaaaXa"), 153)

    def test_single_uppercase_surrounded_by_lowercase(self):
        # Test case 9: Single uppercase character surrounded by lowercase
        # Y=89. Sum = 89
        self.assertEqual(digitSum("zYz"), 89)

    def test_multiple_uppercase_mixed(self):
        # Test case 10: Multiple uppercase characters in a longer string
        # P=80, T=84. Sum = 80+84 = 164
        self.assertEqual(digitSum("PyThon"), 164)