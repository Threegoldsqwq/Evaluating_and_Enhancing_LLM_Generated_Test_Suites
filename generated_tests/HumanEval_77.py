import unittest

class TestIsCube(unittest.TestCase):

    def test_iscube_one(self):
        # Smallest positive cube
        self.assertTrue(iscube(1))

    def test_iscube_minus_one(self):
        # Smallest negative cube (in terms of magnitude)
        self.assertTrue(iscube(-1))

    def test_iscube_zero(self):
        # Zero is a cube
        self.assertTrue(iscube(0))

    def test_iscube_positive_small(self):
        # A small positive perfect cube
        self.assertTrue(iscube(8)) # 2^3

    def test_iscube_negative_small(self):
        # A small negative perfect cube
        self.assertTrue(iscube(-27)) # (-3)^3

    def test_iscube_positive_medium(self):
        # A medium positive perfect cube
        self.assertTrue(iscube(125)) # 5^3

    def test_iscube_positive_large(self):
        # A larger positive perfect cube
        self.assertTrue(iscube(1000)) # 10^3

    def test_iscube_positive_non_cube_small(self):
        # A small positive non-cube
        self.assertFalse(iscube(2))

    def test_iscube_positive_non_cube_close_to_cube(self):
        # A positive non-cube just before a perfect cube
        self.assertFalse(iscube(63)) # close to 4^3 = 64

    def test_iscube_negative_non_cube(self):
        # A negative non-cube
        self.assertFalse(iscube(-10)) # between -8 and -27

    def test_iscube_zero(self):
            """Test with a = 0, which is a perfect cube."""
            self.assertTrue(iscube(0))

    def test_iscube_positive_perfect_cubes(self):
            """Test with various positive perfect cubes."""
            self.assertTrue(iscube(1))
            self.assertTrue(iscube(8))
            self.assertTrue(iscube(27))
            self.assertTrue(iscube(64))
            self.assertTrue(iscube(125))
            self.assertTrue(iscube(729))  # 9^3
            self.assertTrue(iscube(1000)) # 10^3
            self.assertTrue(iscube(1728)) # 12^3
            self.assertTrue(iscube(1331)) # 11^3
            self.assertTrue(iscube(1000000)) # 100^3
            self.assertTrue(iscube(1_000_000_000_000)) # 1,000,000^3, large number test

    def test_iscube_positive_non_cubes(self):
            """Test with various positive non-cube numbers."""
            self.assertFalse(iscube(2))
            self.assertFalse(iscube(7))
            self.assertFalse(iscube(9))
            self.assertFalse(iscube(26))
            self.assertFalse(iscube(28))
            self.assertFalse(iscube(63))
            self.assertFalse(iscube(65))
            self.assertFalse(iscube(999))
            self.assertFalse(iscube(1001))
            self.assertFalse(iscube(1000001)) # Just above a perfect cube
            self.assertFalse(iscube(1_000_000_000_001)) # Large number just above a perfect cube

    def test_iscube_negative_perfect_cubes(self):
            """Test with various negative perfect cubes."""
            self.assertTrue(iscube(-1))
            self.assertTrue(iscube(-8))
            self.assertTrue(iscube(-27))
            self.assertTrue(iscube(-64))
            self.assertTrue(iscube(-125))
            self.assertTrue(iscube(-729))
            self.assertTrue(iscube(-1000))
            self.assertTrue(iscube(-1728))
            self.assertTrue(iscube(-1331))
            self.assertTrue(iscube(-1000000))
            self.assertTrue(iscube(-1_000_000_000_000)) # Large negative cube

    def test_iscube_negative_non_cubes(self):
            """Test with various negative non-cube numbers."""
            self.assertFalse(iscube(-2))
            self.assertFalse(iscube(-7))
            self.assertFalse(iscube(-9))
            self.assertFalse(iscube(-26))
            self.assertFalse(iscube(-28))
            self.assertFalse(iscube(-63))
            self.assertFalse(iscube(-65))
            self.assertFalse(iscube(-999))
            self.assertFalse(iscube(-1001))
            self.assertFalse(iscube(-1000001)) # Just below a negative perfect cube
            self.assertFalse(iscube(-1_000_000_000_001)) # Large number just below a negative perfect cube
# Note: The 'iscube' function is assumed to exist for these tests to run.
# For example:
# def iscube(a: int) -> bool:
#     if a == 0:
#         return True
#     sign = 1 if a > 0 else -1
#     abs_a = abs(a)
#     
#     # Using a simple integer cube root approximation
#     # We can iterate or use a more sophisticated method like binary search
#     # For this problem, a simple loop or a direct calculation is fine.
#     # cube_root = round(abs_a**(1/3))
#     # return (cube_root**3 == abs_a) and (sign * cube_root**3 == a)
#     
#     # More robust integer cube root check to avoid floating point issues
#     low, high = 0, abs_a
#     ans = 0
#     while low <= high:
#         mid = (low + high) // 2
#         mid_cubed = mid * mid * mid
#         if mid_cubed == abs_a:
#             ans = mid
#             break
#         elif mid_cubed < abs_a:
#             low = mid + 1
#         else:
#             high = mid - 1
#     
#     return (ans * ans * ans == abs_a) and (sign * ans * ans * ans == a)

if __name__ == '__main__':
    unittest.main()