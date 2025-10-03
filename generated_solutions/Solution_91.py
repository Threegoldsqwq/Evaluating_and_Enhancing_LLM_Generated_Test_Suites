import re

def is_bored(text: str) -> int:
    """
    Counts the number of "boredoms" in a given text.
    A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.

    Args:
        text: The input string of words.

    Returns:
        The total count of "boredoms".
    """
    boredom_count = 0
    
    # Split the text into potential sentences using regular expressions.
    # The pattern r'[.?!]' matches any of the characters '.', '?', or '!'.
    # re.split removes the delimiters from the resulting parts.
    sentences = re.split(r'[.?!]', text)
    
    for sentence_part in sentences:
        # Clean up each part: remove leading/trailing whitespace.
        # This handles cases where a sentence might start with a space after a delimiter,
        # e.g., "Hello. I am here."
        cleaned_sentence = sentence_part.strip()
        
        # If the cleaned part is empty (e.g., due to multiple delimiters in a row like "Hi!!"),
        # or if it was just whitespace, it's not a valid sentence, so we skip it.
        if not cleaned_sentence:
            continue
            
        # Check if the first word of the sentence is "I".
        # We split the cleaned sentence by spaces to get individual words.
        words = cleaned_sentence.split()
        
        # Ensure there's at least one word in the sentence to avoid index errors.
        # Then check if the first word is exactly "I" (case-sensitive as per problem).
        if words and words[0] == "I":
            boredom_count += 1
            
    return boredom_count