"""
You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.



Example 1:

Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
Example 2:

Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.
Example 3:

Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.


Constraints:

1 <= k <= n <= 1000


Follow up:

Could you solve this problem in less than O(n) complexity?
"""

class Solution:
    """
    Efficencly finds the k-th factor of n by  exploting division paring.
    Time Complexity: O(\sqrt(n))
    """
    def kthFactor(self, n: int, k: int) -> int:
        small, large = [], []
        limit = int(n**0.5)

        # Gahter divisors up to sqrt(n)
        for i in range(1, limit + 1):
            if n%i == 0:
                small.append(i)
                # Avoid double-counting the square root
                if i != n // i:
                    large.append(n//i)
        # small is ascending; large is descending-reverse it
        large.reverse()
        # total ordered list is small+large
        total_divs = len(small) + len(large)
        # if k exceeds total count, no such factor
        if k > total_divs:
            return -1
        if k <= len(small):
            return small[k-1]
        return large[k -1 - len(small)]
