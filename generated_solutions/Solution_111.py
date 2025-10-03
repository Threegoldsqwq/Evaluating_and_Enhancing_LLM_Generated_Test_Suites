from collections import Counter

def histogram(s: str) -> dict:
    """
    Given a string representing space-separated lowercase letters, 
    return a dictionary of the letter(s) with the most repetition 
    and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Examples:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}
    """
    
    # Step 1: Parse the input string into a list of individual letters.
    # s.split() handles multiple spaces correctly and returns an empty list
    # for an empty string or a string with only spaces.
    letters = s.split()

    # Step 2: Handle the empty string case (or string with only spaces).
    # If the list of letters is empty, there are no letters to count.
    if not letters:
        return {}

    # Step 3: Count occurrences of each letter using collections.Counter.
    # This creates a dictionary-like object mapping each letter to its frequency.
    letter_counts = Counter(letters)

    # Step 4: Find the maximum count among all letters.
    # Since 'letters' was not empty, 'letter_counts' will not be empty,
    # so max() on its values is safe.
    max_count = max(letter_counts.values())

    # Step 5: Build the result dictionary.
    # Include only those letters whose count matches the maximum count.
    result_histogram = {}
    for letter, count in letter_counts.items():
        if count == max_count:
            result_histogram[letter] = count
            
    return result_histogram