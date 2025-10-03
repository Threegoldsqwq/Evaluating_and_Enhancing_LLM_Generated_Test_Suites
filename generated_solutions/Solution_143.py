import math

def filter_prime_length_words(sentence: str) -> str:
    """
    Returns a string containing words from the original sentence whose lengths are prime numbers.
    The order of words is preserved.
    """

    def is_prime(n: int) -> bool:
        """
        Checks if a given integer n is a prime number.
        """
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0: # All other even numbers are not prime
            return False
        
        # Check for odd divisors from 3 up to sqrt(n)
        # We only need to check up to the square root of n because if n has a divisor
        # greater than its square root, it must also have a divisor smaller than its square root.
        i = 3
        while i * i <= n: # equivalent to i <= math.sqrt(n)
            if n % i == 0:
                return False
            i += 2 # Only need to check odd divisors
        return True

    words = sentence.split()
    prime_length_words = []

    for word in words:
        if is_prime(len(word)):
            prime_length_words.append(word)

    return " ".join(prime_length_words)