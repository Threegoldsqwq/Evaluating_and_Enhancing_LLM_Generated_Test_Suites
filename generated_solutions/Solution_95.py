def check_dict_case(dict_obj):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if not dict_obj:
        return False

    is_all_lower = True
    is_all_upper = True

    for key in dict_obj.keys():
        # 1. Check if the key is a string
        if not isinstance(key, str):
            return False
        
        # 2. Check if the string key is purely lowercase, purely uppercase, or neither
        if key.islower():
            # If we find a lowercase key, it means not all keys can be uppercase.
            is_all_upper = False
        elif key.isupper():
            # If we find an uppercase key, it means not all keys can be lowercase.
            is_all_lower = False
        else:
            # The key is a string but not purely lower and not purely upper (e.g., "Name", "123", "")
            # This violates the condition.
            return False

    # After checking all keys, return True if all keys were consistently lower
    # OR all keys were consistently upper.
    # If both is_all_lower and is_all_upper are False, it means there was a mix.
    return is_all_lower or is_all_upper