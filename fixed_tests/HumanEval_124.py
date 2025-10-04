import unittest

# Assume the function 'valid_date' is defined elsewhere and imported.
# For the sake of making this test file runnable, I'll include a dummy function
# but in a real scenario, it would be imported.
# def valid_date(date_string: str) -> bool:
#     # Dummy implementation for testing purposes
#     # In reality, this would be the function you are testing
#     if not date_string:
#         return False
#     if date_string == '03-11-2000': return True
#     if date_string == '12-31-2023': return True
#     if date_string == '04-30-2023': return True
#     if date_string == '02-29-2024': return True # As per rule, Feb max 29
#
#     parts = date_string.split('-')
#     if len(parts) != 3: return False
#
#     try:
#         month = int(parts[0])
#         day = int(parts[1])
#         year = int(parts[2])
#     except ValueError:
#         return False
#
#     if not (1 <= month <= 12): return False
#     if not (1 <= day): return False # Check lower bound, upper bound handled by month
#
#     # Month-specific day validation
#     days_in_month = {
#         1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31,
#         4: 30, 6: 30, 9: 30, 11: 30,
#         2: 29 # Rule states 29 for Feb, no leap year logic needed
#     }
#
#     if day > days_in_month.get(month, 0): return False
#
#     # Check format mm-dd-yyyy implies leading zeros
#     if len(parts[0]) != 2 or len(parts[1]) != 2 or len(parts[2]) != 4: return False
#
#     return True


class TestValidDate(unittest.TestCase):

    def test_01_basic_valid_date(self):
        # Example from problem description
        self.assertTrue(valid_date('03-11-2000'))

    def test_02_valid_end_of_month_31_days(self):
        # Test valid date for a 31-day month at its limit
        self.assertTrue(valid_date('12-31-2023'))

    def test_03_valid_end_of_month_30_days(self):
        # Test valid date for a 30-day month at its limit
        self.assertTrue(valid_date('04-30-2023'))

    def test_04_valid_end_of_february(self):
        # Test valid date for February at its limit (29 days as per rule)
        self.assertTrue(valid_date('02-29-2024'))

    def test_05_invalid_format_wrong_delimiter(self):
        # Example from problem description
        self.assertFalse(valid_date('06/04/2020'))

    def test_06_invalid_month_too_high(self):
        # Example from problem description
        self.assertFalse(valid_date('15-01-2012'))

    def test_07_invalid_day_zero_or_too_low(self):
        # Example from problem description (04-0-2040 suggests day '0')
        self.assertFalse(valid_date('04-00-2040'))
        self.assertFalse(valid_date('04-0-2040')) # Also tests format 'dd'

    def test_08_invalid_day_too_high_for_31_day_month(self):
        # Day 32 in a 31-day month
        self.assertFalse(valid_date('01-32-2023'))

    def test_09_invalid_day_too_high_for_30_day_month(self):
        # Day 31 in a 30-day month
        self.assertFalse(valid_date('06-31-2023'))

    def test_10_invalid_day_too_high_for_february(self):
        # Day 30 in February (rule states max 29)
        self.assertFalse(valid_date('02-30-2024'))

    # Additional tests for comprehensive coverage (if more than 10 were allowed)
    # def test_11_empty_string(self):
    #     self.assertFalse(valid_date(''))
    #
    # def test_12_invalid_month_zero(self):
    #     self.assertFalse(valid_date('00-15-2023'))
    #
    # def test_13_invalid_format_month_not_two_digits(self):
    #     self.assertFalse(valid_date('3-11-2000'))
    #
    # def test_14_invalid_format_day_not_two_digits(self):
    #     self.assertFalse(valid_date('03-1-2000'))
    #
    # def test_15_invalid_format_non_numeric_parts(self):
    #     self.assertFalse(valid_date('XX-11-2000'))
    #     self.assertFalse(valid_date('03-YY-2000'))
    #     self.assertFalse(valid_date('03-11-ZZZZ'))

if __name__ == '__main__':
    # This is a placeholder for the actual function.
    # In a real setup, `valid_date` would be imported.
    # For these tests to run, you would need to define or import valid_date.
    # Here's a sample implementation just so the tests can execute for demonstration.
    # def valid_date(date_string: str) -> bool:
    #     """
    #     Validates a given date string based on specified rules.
    #     """
    #     if not date_string:
    #         return False

    #     parts = date_string.split('-')

    #     # Rule 4: The date should be in the format: mm-dd-yyyy
    #     if len(parts) != 3:
    #         return False

    #     try:
    #         month_str, day_str, year_str = parts
    #         month = int(month_str)
    #         day = int(day_str)
    #         year = int(year_str) # Year itself is not validated beyond being int and 4 digits
    #     except ValueError:
    #         return False # Non-numeric parts

    #     # Check format: mm, dd, yyyy lengths
    #     if not (len(month_str) == 2 and len(day_str) == 2 and len(year_str) == 4):
    #         return False

    #     # Rule 3: The months should not be less than 1 or higher than 12.
    #     if not (1 <= month <= 12):
    #         return False

    #     # Rule 2: The number of days validation
    #     # First, ensure day is at least 1
    #     if day < 1:
    #         return False

    #     days_in_month = {
    #         1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31, # 31-day months
    #         4: 30, 6: 30, 9: 30, 11: 30, # 30-day months
    #         2: 29 # February, fixed at 29 days as per problem statement (no leap year logic)
    #     }

    #     max_days = days_in_month.get(month, 0)
    #     if max_days == 0: # Should not happen if month is 1-12, but good for robustness
    #         return False
        
    #     if day > max_days:
    #         return False

    #     return True

    unittest.main(argv=['first-arg-is-ignored'], exit=False)