def words_string(words_str: str) -> list[str]:
    """
    Splits a string of words into an array of words, using commas or spaces
    as delimiters.

    Args:
        words_str: The input string containing words separated by commas or spaces.

    Returns:
        A list of words extracted from the input string.

    Examples:
        words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
        words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
        words_string("") == []
        words_string("  word1,word2  ") == ["word1", "word2"]
        words_string("singleword") == ["singleword"]
    """
    # Step 1: Replace all commas with spaces.
    # This turns "Hi, my" into "Hi  my", "One,two" into "One two".
    normalized_str = words_str.replace(',', ' ')

    # Step 2: Split the normalized string by whitespace.
    # The `split()` method (without arguments) handles multiple spaces
    # and leading/trailing spaces gracefully, returning only non-empty words.
    words_array = normalized_str.split()

    return words_array