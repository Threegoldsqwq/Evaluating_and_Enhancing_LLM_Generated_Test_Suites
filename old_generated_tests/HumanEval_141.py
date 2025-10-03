import unittest

class TestFileNameCheck(unittest.TestCase):

    # Assume the function file_name_check is defined elsewhere and imported.
    # For testing purposes, we might define a dummy one or assume it's available.
    # def file_name_check(self, file_name):
    #     # Placeholder for the actual function for testing
    #     # Implement the logic here if running tests stand-alone without the actual function
    #     pass

    def test_valid_basic(self):
        """Test a basic valid file name."""
        self.assertEqual(file_name_check("example.txt"), 'Yes')

    def test_valid_with_capital_and_digits(self):
        """Test a valid file name with capital letters and digits (up to 3)."""
        self.assertEqual(file_name_check("MyDoc12.dll"), 'Yes')

    def test_valid_max_three_digits(self):
        """Test a valid file name with exactly three digits."""
        self.assertEqual(file_name_check("picture123.exe"), 'Yes')

    def test_invalid_starts_with_digit(self):
        """Test case where name starts with a digit."""
        self.assertEqual(file_name_check("1myfile.txt"), 'No')

    def test_invalid_too_many_digits(self):
        """Test case with more than three digits."""
        self.assertEqual(file_name_check("report1234.txt"), 'No')

    def test_invalid_no_dot(self):
        """Test case with no dot in the file name."""
        self.assertEqual(file_name_check("nodotfile"), 'No')

    def test_invalid_two_dots(self):
        """Test case with more than one dot."""
        self.assertEqual(file_name_check("file.name.txt"), 'No')

    def test_invalid_empty_before_dot(self):
        """Test case with an empty string before the dot."""
        self.assertEqual(file_name_check(".txt"), 'No')

    def test_invalid_bad_extension(self):
        """Test case with an invalid file extension."""
        self.assertEqual(file_name_check("document.pdf"), 'No')

    def test_invalid_case_sensitive_extension(self):
        """Test case where extension is valid but with wrong case (should be exact match)."""
        self.assertEqual(file_name_check("archive.TXT"), 'No')