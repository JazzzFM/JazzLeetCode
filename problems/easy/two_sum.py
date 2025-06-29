from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Given a list of integers `nums` and an integer `target`, return
        the indices of the two numbers that add up to `target`.

        Time complexity: O(n) — we traverse the list only once.
        Space complexity: O(n) — we store values in a hash map.

        Scientific rationale:
        - A single pass with a hash map exploits O(1) access time.
        - It minimizes redundant operations and enables early discovery.

        Stoic insight:
        - “Nature loves simplicity.” — Seneca
        - We adopt the cleanest, most direct solution, avoiding unnecessary complexity.

        :param nums: List[int] — array of integers
        :param target: int — target sum
        :return: List[int] — indices of the two elements that sum to `target`
        """
        # Create a map from value to its index for instant lookup
        complement_map = {}

        for idx, num in enumerate(nums):
            complement = target - num
            # If we've already seen the complement, return the result
            if complement in complement_map:
                # Justification: found both values in a single pass
                return [complement_map[complement], idx]
            # Store the index of the current number
            complement_map[num] = idx

        # According to the prompt, there is always exactly one valid solution
        raise ValueError("No two sum solution found")

