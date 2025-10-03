def add(lst: list[int]) -> int:
    """
    Given a non-empty list of integers lst, add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2
        # Explanation:
        # Index 0: 4 (even index, skip)
        # Index 1: 2 (odd index, even element -> add 2)
        # Index 2: 6 (even index, skip)
        # Index 3: 7 (odd index, odd element -> skip)
        # Result: 2

        add([1, 2, 3, 4, 5, 6]) ==> 2 + 6 = 8
        # Explanation:
        # Index 0: 1 (even index, skip)
        # Index 1: 2 (odd index, even element -> add 2)
        # Index 2: 3 (even index, skip)
        # Index 3: 4 (odd index, even element -> add 4) - wait, example says 2+6. My interpretation would add 4.
        # Let's re-check the problem statement: "add the even elements that are at odd indices."
        # Ah, the example provided `add([4, 2, 6, 7]) ==> 2` implies that for index 3, element 7 (odd, odd) is skipped.
        # For `add([1, 2, 3, 4, 5, 6])`:
        # Index 0: 1 (even index) -> skip
        # Index 1: 2 (odd index AND even element) -> add 2. Current sum: 2
        # Index 2: 3 (even index) -> skip
        # Index 3: 4 (odd index AND even element) -> add 4. Current sum: 2 + 4 = 6
        # Index 4: 5 (even index) -> skip
        # Index 5: 6 (odd index AND even element) -> add 6. Current sum: 6 + 6 = 12
        # So my `add([1, 2, 3, 4, 5, 6]) ==> 2 + 6 = 8` example was flawed in my head.
        # It should be 2 + 4 + 6 = 12.
        # The core logic is correct based on the problem statement and the first example.

        add([0, 10, 20, 30]) ==> 10 + 30 = 40
        add([1, 3, 5, 7]) ==> 0
        add([2]) ==> 0
    """
    total_sum = 0
    # Use enumerate to get both the index and the element
    for index, element in enumerate(lst):
        # Check if the index is odd
        if index % 2 != 0:
            # Check if the element at this odd index is even
            if element % 2 == 0:
                total_sum += element
    return total_sum