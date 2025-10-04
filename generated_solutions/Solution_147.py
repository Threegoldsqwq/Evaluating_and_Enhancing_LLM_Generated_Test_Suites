import math


def get_max_triples(self, n: int) -> int:
        # Step 1: Analyze a[x] = x*x - x + 1 modulo 3.
        # a[x] = x*(x-1) + 1
        #
        # - If x % 3 == 0: a[x] % 3 = (0 * (0-1) + 1) % 3 = 1
        # - If x % 3 == 1: a[x] % 3 = (1 * (1-1) + 1) % 3 = 1
        # - If x % 3 == 2: a[x] % 3 = (2 * (2-1) + 1) % 3 = (2 * 1 + 1) % 3 = 0
        #
        # In summary:
        # a[x] % 3 == 0 if x % 3 == 2
        # a[x] % 3 == 1 if x % 3 == 0 or x % 3 == 1

        # Step 2: Count the number of integers i from 1 to n for each remainder modulo 3.
        # This is an O(1) calculation for large n.
        
        # Base count for each remainder (n // 3 full cycles of 0, 1, 2)
        count_i_rem0 = n // 3  # Count of i such that i % 3 == 0
        count_i_rem1 = n // 3  # Count of i such that i % 3 == 1
        count_i_rem2 = n // 3  # Count of i such that i % 3 == 2

        # Adjust counts for the remaining elements (n % 3)
        remainder = n % 3
        if remainder >= 1:
            # If n ends with a number like ...3k+1, count_i_rem1 gets one more
            # Example: n=4 -> i=1,4 both have rem 1.
            count_i_rem1 += 1
        if remainder >= 2:
            # If n ends with a number like ...3k+2, count_i_rem2 gets one more
            # Example: n=5 -> i=2,5 both have rem 2.
            count_i_rem2 += 1

        # Step 3: Map these counts to the remainders of a[p].
        # num_a_rem0: Count of a[p] such that a[p] % 3 == 0.
        # This occurs when p % 3 == 2.
        num_a_rem0 = count_i_rem2
        
        # num_a_rem1: Count of a[p] such that a[p] % 3 == 1.
        # This occurs when p % 3 == 0 or p % 3 == 1.
        num_a_rem1 = count_i_rem0 + count_i_rem1

        # Step 4: Calculate the number of triples (a[i], a[j], a[k]) such that i < j < k
        # and (a[i] + a[j] + a[k]) % 3 == 0.
        # This means (a[i]%3 + a[j]%3 + a[k]%3) % 3 == 0.
        
        # The possible remainders for a[p] are only 0 or 1.
        # There are two scenarios where the sum of three remainders is 0 mod 3:
        #
        # Scenario 1: All three a[p] values are 0 mod 3.
        # (0 + 0 + 0) % 3 == 0.
        # We need to choose 3 elements from the 'num_a_rem0' available elements.
        triples_0_mod_3 = 0
        if num_a_rem0 >= 3:
            # C(m, 3) = m * (m - 1) * (m - 2) / 6
            triples_0_mod_3 = (num_a_rem0 * (num_a_rem0 - 1) * (num_a_rem0 - 2)) // 6

        # Scenario 2: All three a[p] values are 1 mod 3.
        # (1 + 1 + 1) % 3 == 0.
        # We need to choose 3 elements from the 'num_a_rem1' available elements.
        triples_1_mod_3 = 0
        if num_a_rem1 >= 3:
            triples_1_mod_3 = (num_a_rem1 * (num_a_rem1 - 1) * (num_a_rem1 - 2)) // 6

        # No other combinations (e.g., 0+0+1, 0+1+1) result in a sum that is a multiple of 3.

        return triples_0_mod_3 + triples_1_mod_3