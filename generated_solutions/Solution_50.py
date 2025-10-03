import string

# Define the shift value and alphabet size as constants for clarity and easy modification
SHIFT_VALUE = 5
ALPHABET_SIZE = 26

def encode_shift(text: str) -> str:
    """
    Returns an encoded string by shifting every alphabetic character by SHIFT_VALUE
    positions forward in the alphabet. Non-alphabetic characters are unchanged.
    Case is preserved, and the shift wraps around the alphabet (e.g., 'z' shifted
    by 5 becomes 'e').

    Args:
        text (str): The input string to encode.

    Returns:
        str: The encoded string.
    """
    encoded_chars = []
    for char in text:
        if 'a' <= char <= 'z':
            # Handle lowercase letters:
            # 1. Get its 0-indexed position in the alphabet (0 for 'a', 25 for 'z').
            # 2. Add the SHIFT_VALUE.
            # 3. Use modulo 26 to wrap around if it goes beyond 'z'.
            # 4. Add back the ASCII value of 'a' to get the new character's ASCII.
            start_ascii = ord('a')
            shifted_position = (ord(char) - start_ascii + SHIFT_VALUE) % ALPHABET_SIZE
            encoded_chars.append(chr(start_ascii + shifted_position))
        elif 'A' <= char <= 'Z':
            # Handle uppercase letters similarly
            start_ascii = ord('A')
            shifted_position = (ord(char) - start_ascii + SHIFT_VALUE) % ALPHABET_SIZE
            encoded_chars.append(chr(start_ascii + shifted_position))
        else:
            # Non-alphabetic characters remain unchanged
            encoded_chars.append(char)
    return "".join(encoded_chars)

def decode_shift(encoded_text: str) -> str:
    """
    Takes a string encoded with the encode_shift function and returns the
    original decoded string. It shifts every alphabetic character by SHIFT_VALUE
    positions backward in the alphabet. Non-alphabetic characters are unchanged.
    Case is preserved, and the shift wraps around the alphabet (e.g., 'e'
    shifted back by 5 becomes 'z').

    Args:
        encoded_text (str): The string encoded with encode_shift.

    Returns:
        str: The decoded (original) string.
    """
    decoded_chars = []
    for char in encoded_text:
        if 'a' <= char <= 'z':
            # Handle lowercase letters:
            # 1. Get its 0-indexed position.
            # 2. Subtract the SHIFT_VALUE.
            # 3. Use modulo 26. Python's modulo operator handles negative numbers
            #    correctly for this wrapping scenario (e.g., (-5 % 26) is 21).
            # 4. Add back the ASCII value of 'a'.
            start_ascii = ord('a')
            shifted_position = (ord(char) - start_ascii - SHIFT_VALUE) % ALPHABET_SIZE
            decoded_chars.append(chr(start_ascii + shifted_position))
        elif 'A' <= char <= 'Z':
            # Handle uppercase letters similarly
            start_ascii = ord('A')
            shifted_position = (ord(char) - start_ascii - SHIFT_VALUE) % ALPHABET_SIZE
            decoded_chars.append(chr(start_ascii + shifted_position))
        else:
            # Non-alphabetic characters remain unchanged
            decoded_chars.append(char)
    return "".join(decoded_chars)

# --- Example Usage ---
if __name__ == "__main__":
    original_string = "Hello, World! This is a test. 123 ABC-XYZ."

    # Encode the string
    encoded_string = encode_shift(original_string)
    print(f"Original: {original_string}")
    print(f"Encoded:  {encoded_string}")

    # Decode the encoded string
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded:  {decoded_string}")

    # Test with edge cases (wrapping)
    wrap_test_original = "abc xyz ABC XYZ"
    wrap_test_encoded = encode_shift(wrap_test_original)
    wrap_test_decoded = decode_shift(wrap_test_encoded)
    print(f"\nWrap Test Original: {wrap_test_original}")
    print(f"Wrap Test Encoded:  {wrap_test_encoded}") # Expected: "fgh cde FGH CDE"
    print(f"Wrap Test Decoded:  {wrap_test_decoded}") # Expected: "abc xyz ABC XYZ"

    assert encoded_string == "Mjqqt, Btwqi! Ymnx nx f yjxy. 123 FGH-CDE."
    assert decoded_string == original_string
    assert wrap_test_encoded == "fgh cde FGH CDE"
    assert wrap_test_decoded == wrap_test_original
    print("\nAll assertions passed!")