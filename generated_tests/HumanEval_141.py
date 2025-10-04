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
    def test_digit_count_exceeds_three(self):
            # Condition 1: More than three digits
            self.assertEqual(file_name_check("file1234.txt"), 'No')
            self.assertEqual(file_name_check("12345.exe"), 'No')
            self.assertEqual(file_name_check("a1b2c3d4.dll"), 'No')
            self.assertEqual(file_name_check("report_0123_final.txt"), 'No')

    def test_invalid_dot_count(self):
            # Condition 2: Not exactly one dot
            self.assertEqual(file_name_check("nofilewithnodot"), 'No') # Zero dots
            self.assertEqual(file_name_check("my.file.txt"), 'No') # Two dots
            self.assertEqual(file_name_check("another.test.file.exe"), 'No') # Multiple dots

    def test_empty_prefix(self):
            # Condition 3a: The substring before the dot is empty
            self.assertEqual(file_name_check(".txt"), 'No')
            self.assertEqual(file_name_check(".exe"), 'No')
            self.assertEqual(file_name_check(".dll"), 'No')

    def test_prefix_starts_with_non_letter(self):
            # Condition 3b: The substring before the dot does not start with a letter
            self.assertEqual(file_name_check("1file.txt"), 'No') # Starts with digit
            self.assertEqual(file_name_check("_file.exe"), 'No') # Starts with underscore
            self.assertEqual(file_name_check("-document.dll"), 'No') # Starts with hyphen
            self.assertEqual(file_name_check(" file.txt"), 'No') # Starts with space
            self.assertEqual(file_name_check("$report.exe"), 'No') # Starts with symbol

    def test_invalid_extension(self):
            # Condition 4: The substring after the dot is not one of ['txt', 'exe', 'dll']
            self.assertEqual(file_name_check("image.jpg"), 'No')
            self.assertEqual(file_name_check("archive.zip"), 'No')
            self.assertEqual(file_name_check("document.pdf"), 'No')
            self.assertEqual(file_name_check("file."), 'No') # Empty extension
            self.assertEqual(file_name_check("file.TXT"), 'No') # Case sensitive extension
            self.assertEqual(file_name_check("file.TxT"), 'No') # Case sensitive extension

    def test_valid_file_names(self):
            # Valid cases covering various acceptable scenarios
            self.assertEqual(file_name_check("myfile.txt"), 'Yes') # No digits
            self.assertEqual(file_name_check("file1.exe"), 'Yes') # One digit
            self.assertEqual(file_name_check("doc12.dll"), 'Yes') # Two digits
            self.assertEqual(file_name_check("report123.txt"), 'Yes') # Three digits
            self.assertEqual(file_name_check("A_document.exe"), 'Yes') # Starts with uppercase letter
            self.assertEqual(file_name_check("z_file.dll"), 'Yes') # Starts with lowercase letter
            self.assertEqual(file_name_check("My_File_Name_with_spaces.txt"), 'Yes') # Spaces and underscores in prefix
            self.assertEqual(file_name_check("file-name-with-hyphens.exe"), 'Yes') # Hyphens in prefix
            self.assertEqual(file_name_check("anotherfilewith.dots.in.name.txt"), 'Yes') # Dots in prefix (only one final dot)
            self.assertEqual(file_name_check("file001.dll"), 'Yes') # Digits at start of prefix after first letter (e.g., 'f001ile')
            self.assertEqual(file_name_check("f001ile.txt"), 'Yes') # Mixed digits and letters in prefix
            self.assertEqual(file_name_check("maxdigits123.exe"), 'Yes') # Max allowed digits
            self.assertEqual(file_name_check("min.txt"), 'Yes') # Minimal valid prefix
            self.assertEqual(file_name_check("a.txt"), 'Yes') # Single character prefix
            self.assertEqual(file_name_check("b.exe"), 'Yes')
            self.assertEqual(file_name_check("c.dll"), 'Yes')
