def compare(scores: list[int], guesses: list[int]) -> list[int]:
    """
    Compares a list of actual scores with a list of guesses and returns a list
    indicating how far off each guess was.

    Args:
        scores: A list of integers representing the actual scores of matches.
        guesses: A list of integers representing the guessed scores for the same matches.
                 It is guaranteed that 'scores' and 'guesses' are of equal length.

    Returns:
        A list of integers, where each element is 0 if the guess was correct,
        or the absolute difference between the score and the guess otherwise.
    """
    # Initialize an empty list to store the results of the comparison
    differences = []

    # Iterate through both lists simultaneously using zip()
    # zip() pairs up elements from scores and guesses at the same index
    for score, guess in zip(scores, guesses):
        if score == guess:
            # If the guess is correct, the difference is 0
            differences.append(0)
        else:
            # If the guess is incorrect, calculate the absolute difference
            # The absolute difference ensures the result is always non-negative
            differences.append(abs(score - guess))

    return differences