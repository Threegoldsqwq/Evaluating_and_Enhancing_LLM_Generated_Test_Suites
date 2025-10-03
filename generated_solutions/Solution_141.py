def file_name_check(file_name: str) -> str:
    """
    Checks if a given file name is valid based on specific criteria.

    A file name is valid if:
    - It contains not more than three digits.
    - It contains exactly one dot '.'.
    - The substring before the dot is not empty and starts with a letter.
    - The substring after the dot is one of ['txt', 'exe', 'dll'].

    Args:
        file_name (str): The string representing the file's name.

    Returns:
        str: 'Yes' if the file name is valid, 'No' otherwise.
    """

    # Condition 1: There should not be more than three digits ('0'-'9')
    digit_count = 0
    for char in file_name:
        if char.isdigit():
            digit_count += 1
    if digit_count > 3:
        return 'No'

    # Condition 2: The file's name contains exactly one dot '.'
    if file_name.count('.') != 1:
        return 'No'

    # Split the file name into two parts based on the dot
    # We are sure file_name contains exactly one dot at this point
    parts = file_name.split('.')
    prefix = parts[0]
    extension = parts[1]

    # Condition 3a: The substring before the dot should not be empty
    if not prefix:  # Equivalent to len(prefix) == 0
        return 'No'

    # Condition 3b: The substring before the dot starts with a letter
    # 'isalpha()' checks for letters from the latin alphabet.
    if not prefix[0].isalpha():
        return 'No'

    # Condition 4: The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    allowed_extensions = ['txt', 'exe', 'dll']
    if extension not in allowed_extensions:
        return 'No'

    # If all conditions are met, the file name is valid
    return 'Yes'