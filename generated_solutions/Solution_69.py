import collections

def search(nums: list[int]) -> int:
    """
    Given a non-empty list of positive integers, return the greatest integer that is 
    greater than zero, and has a frequency greater than or equal to the value of the 
    integer itself.
    If no such a value exist, return -1.
    """
    # 1. Calculate frequencies of each number in the list.
    # collections.Counter is an efficient way to do this.
    counts = collections.Counter(nums)

    # 2. Initialize a variable to store the greatest qualifying integer found so far.
    #    Start with -1, as per the problem's requirement for no such value existing.
    max_qualifying_int = -1

    # 3. Iterate through the unique numbers (keys) and their frequencies (values)
    #    in the counts dictionary.
    for num, freq in counts.items():
        # The problem states "positive integers", so num will always be > 0.
        # Check the condition: frequency >= value of the integer itself.
        if freq >= num:
            # If the condition is met, 'num' is a candidate.
            # We want the *greatest* such integer, so we update max_qualifying_int
            # if the current 'num' is larger.
            max_qualifying_int = max(max_qualifying_int, num)
            
    # 4. Return the greatest qualifying integer found, or -1 if no such integer was found.
    return max_qualifying_int