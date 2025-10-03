def Strongest_Extension(class_name: str, extensions: list[str]) -> str:
    """
    Finds the strongest extension for a given class name based on a strength calculation.

    The strength of an extension is calculated as (number of uppercase letters) -
    (number of lowercase letters). If multiple extensions have the same maximum strength,
    the one that appears first in the list is chosen.

    Args:
        class_name: The name of the base class.
        extensions: A list of extension names (strings).

    Returns:
        A string in the format "ClassName.StrongestExtensionName".

    Raises:
        ValueError: If the extensions list is empty, as a strongest extension
                    cannot be determined.
    """
    if not extensions:
        # Handle the case of an empty extensions list.
        # According to the problem statement, there should be an extension to find.
        # Raising an error is a robust way to handle this unexpected input.
        raise ValueError("Extensions list cannot be empty. At least one extension is required.")

    # Initialize with the first extension's strength and name.
    # This automatically handles the "first in list" tie-breaking rule.
    strongest_ext_name = extensions[0]
    
    # Calculate initial strength for the first extension
    cap_initial = sum(1 for char in strongest_ext_name if char.isupper())
    sm_initial = sum(1 for char in strongest_ext_name if char.islower())
    max_strength = cap_initial - sm_initial

    # Iterate through the rest of the extensions (starting from the second one)
    for i in range(1, len(extensions)):
        current_ext_name = extensions[i]
        
        # Calculate strength for the current extension
        cap_current = sum(1 for char in current_ext_name if char.isupper())
        sm_current = sum(1 for char in current_ext_name if char.islower())
        current_strength = cap_current - sm_current

        # If the current extension is strictly stronger, update our tracking variables.
        # If current_strength == max_strength, we don't update, preserving the
        # extension that appeared earlier in the list.
        if current_strength > max_strength:
            max_strength = current_strength
            strongest_ext_name = current_ext_name

    # Format and return the result string
    return f"{class_name}.{strongest_ext_name}"