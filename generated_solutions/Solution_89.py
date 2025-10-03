import string

def encrypt(text: str) -> str:
    """
    Encrypts a string by rotating the alphabet.
    Letters shift down by 2 * 2 = 4 places.
    Non-alphabetic characters are left unchanged.
    Case of letters is preserved.

    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    encrypted_chars = []
    # The shift amount is "two multiplied to two places" which is 2 * 2 = 4
    shift = 4
    
    # Use string.ascii_lowercase for a reliable alphabet reference
    # string.ascii_lowercase contains 'abcdefghijklmnopqrstuvwxyz'

    for char in text:
        if char.isalpha():
            # Determine if the original character was uppercase
            is_uppercase = char.isupper()
            
            # Convert to lowercase to find its position in the alphabet
            lower_char = char.lower()
            
            # Find the 0-based index of the character in the lowercase alphabet
            # string.ascii_lowercase.find() returns -1 if not found, 
            # but we've already checked that char is an alphabet letter.
            original_index = string.ascii_lowercase.find(lower_char)
            
            # Calculate the new index after applying the shift.
            # The modulo operator (%) ensures the index wraps around the 26-letter alphabet.
            new_index = (original_index + shift) % 26
            
            # Get the new character from the lowercase alphabet using the new index
            new_lower_char = string.ascii_lowercase[new_index]
            
            # If the original character was uppercase, convert the new character back to uppercase
            if is_uppercase:
                encrypted_chars.append(new_lower_char.upper())
            else:
                encrypted_chars.append(new_lower_char)
        else:
            # If the character is not an alphabet letter (e.g., space, number, symbol),
            # append it to the result without modification.
            encrypted_chars.append(char)
            
    # Join all processed characters to form the final encrypted string
    return "".join(encrypted_chars)