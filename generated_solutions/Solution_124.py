def valid_date(date_string: str) -> bool:
    """
    Validates a given date string based on specific rules.

    Args:
        date_string: The date string to validate, expected in 'mm-dd-yyyy' format.

    Returns:
        True if the date is valid according to all rules, False otherwise.
    """

    # Rule 1: The date string is not empty.
    if not date_string:
        return False

    # Rule 4: The date should be in the format: mm-dd-yyyy
    # Check total length first.
    if len(date_string) != 10:
        return False

    # Check for correct hyphen separators.
    if date_string[2] != '-' or date_string[5] != '-':
        return False

    # Split the string into month, day, and year parts.
    parts = date_string.split('-')

    # After splitting by hyphens, there should be exactly 3 parts.
    # This is a defensive check, as length and hyphen checks already largely ensure this.
    if len(parts) != 3:
        return False

    month_str, day_str, year_str = parts[0], parts[1], parts[2]

    # Rule 4 (continued): Ensure each part consists of digits and has the correct length.
    if not (month_str.isdigit() and len(month_str) == 2):
        return False
    if not (day_str.isdigit() and len(day_str) == 2):
        return False
    if not (year_str.isdigit() and len(year_str) == 4):
        return False

    # Convert parts to integers. This should be safe now given the isdigit() checks.
    try:
        month = int(month_str)
        day = int(day_str)
        year = int(year_str)  # Year is not explicitly validated beyond format, but parsed.
    except ValueError:
        # This block should ideally not be reached if `isdigit()` checks are thorough,
        # but provides an extra layer of safety.
        return False

    # Rule 3: The months should not be less than 1 or higher than 12.
    if not (1 <= month <= 12):
        return False

    # Rule 2: Validate the number of days.
    # First, ensure the day is not less than 1.
    if day < 1:
        return False

    # Define the maximum days for different month categories.
    months_31_days = {1, 3, 5, 7, 8, 10, 12}
    months_30_days = {4, 6, 9, 11}
    max_days_february = 29 # As per problem statement, no leap year logic required.

    if month in months_31_days:
        if day > 31:
            return False
    elif month in months_30_days:
        if day > 30:
            return False
    elif month == 2:  # February
        if day > max_days_february:
            return False
    # No 'else' branch is needed here for `month` because Rule 3 already ensures `1 <= month <= 12`
    # and all months are covered by the `months_31_days`, `months_30_days`, or `month == 2` conditions.

    # If all checks pass, the date string is considered valid.
    return True