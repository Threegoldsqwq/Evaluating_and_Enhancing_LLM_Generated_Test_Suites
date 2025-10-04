import unittest

# Assume the Solution class with the solve method exists as described in the problem.
# For the purpose of running these tests, a mock Solution class might be helpful
# during development, but for the submission, we just assume it's available.

class Solution:
    """
    Dummy Solution class to satisfy the test structure. 
    The actual implementation would be provided separately.
    """
    def combinations(self, n, k):
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1
        if k > n // 2:
            k = n - k
        
        res = 1
        for i in range(k):
            res = res * (n - i) // (i + 1)
        return res

    def solve(self, n: int) -> int:
        if n < 3:
            return 0

        # a[i] = i * i - i + 1 (using 1-indexed i)
        # Let's analyze a[i] % 3:
        # If i % 3 == 0: i = 3k. a[i] = 3k(3k-1) + 1. a[i] % 3 = 1.
        # If i % 3 == 1: i = 3k+1. a[i] = (3k+1)(3k) + 1. a[i] % 3 = 1.
        # If i % 3 == 2: i = 3k+2. a[i] = (3k+2)(3k+1) + 1 = (9k^2 + 9k + 2) + 1. a[i] % 3 = 0.

        # So, a[i] % 3 is 0 if i % 3 == 2 (for 1-indexed i)
        # And a[i] % 3 is 1 if i % 3 == 0 or i % 3 == 1 (for 1-indexed i)

        # Count of numbers whose remainder modulo 3 is 0 (c0)
        # These are a[i] where i % 3 == 2. (i = 2, 5, 8, ...)
        # The number of such 'i' up to 'n' is (n + 1) // 3
        c0 = (n + 1) // 3 

        # Count of numbers whose remainder modulo 3 is 1 (c1)
        # These are a[i] where i % 3 == 0 or i % 3 == 1.
        # Count of i where i % 3 == 0 (i = 3, 6, 9, ...) is n // 3
        # Count of i where i % 3 == 1 (i = 1, 4, 7, ...) is (n + 2) // 3
        c1 = (n // 3) + ((n + 2) // 3)

        # We need (a[i] + a[j] + a[k]) % 3 == 0.
        # Since a[x] % 3 can only be 0 or 1, the possible combinations of remainders (mod 3) are:
        # (0, 0, 0) -> sum % 3 = 0
        # (1, 1, 1) -> sum % 3 = 3, which is 0 % 3
        # Other combinations involving 0s and 1s like (0,0,1) or (0,1,1) won't sum to 0 mod 3.
        # Also, no elements have a remainder of 2 mod 3.

        # So, the total number of triples is C(c0, 3) + C(c1, 3)
        
        result = self.combinations(c0, 3) + self.combinations(c1, 3)
        return result


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_n_1(self):
        # n=1, no triples possible
        self.assertEqual(self.solution.solve(1), 0)

    def test_n_2(self):
        # n=2, no triples possible
        self.assertEqual(self.solution.solve(2), 0)
        
    def test_n_3(self):
        # n=3, a = [1, 3, 7]. a_mod_3 = [1, 0, 1]. c0=1, c1=2. C(1,3)+C(2,3) = 0.
        self.assertEqual(self.solution.solve(3), 0)

    def test_n_4(self):
        # n=4, a = [1, 3, 7, 13]. a_mod_3 = [1, 0, 1, 1]. c0=1, c1=3. C(1,3)+C(3,3) = 0+1 = 1.
        self.assertEqual(self.solution.solve(4), 1)

    def test_n_5_example(self):
        # n=5, a = [1, 3, 7, 13, 21]. a_mod_3 = [1, 0, 1, 1, 0]. c0=2, c1=3. C(2,3)+C(3,3) = 0+1 = 1.
        self.assertEqual(self.solution.solve(5), 1)

    def test_n_6(self):
        # n=6, c0=2, c1=4. C(2,3)+C(4,3) = 0+4 = 4.
        self.assertEqual(self.solution.solve(6), 4)

    def test_n_8(self):
        # n=8, c0=3, c1=5. C(3,3)+C(5,3) = 1+10 = 11. (First case where C(c0,3) is non-zero)
        self.assertEqual(self.solution.solve(8), 11)

    def test_n_9(self):
        # n=9, c0=3, c1=6. C(3,3)+C(6,3) = 1+20 = 21.
        self.assertEqual(self.solution.solve(9), 21)

    def test_n_100_medium_large(self):
        # n=100, c0=33, c1=67. C(33,3)+C(67,3) = 5456 + 47855 = 53311.
        self.assertEqual(self.solution.solve(100), 53311)

    def test_n_1000_large(self):
        # n=1000, c0=333, c1=667. C(333,3)+C(667,3) = 6099666 + 49208055 = 55307721.
        self.assertEqual(self.solution.solve(1000), 55307721)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)