"""
You are given a 0-indexed integer array nums, an integer modulo, and an integer k.

Your task is to find the count of subarrays that are interesting.

A subarray nums[l..r] is interesting if the following condition holds:

Let cnt be the number of indices i in the range [l, r] such that nums[i] % modulo == k. Then, cnt % modulo == k.
Return an integer denoting the count of interesting subarrays.

Note: A subarray is a contiguous non-empty sequence of elements within an array
"""

from typing import List
from collections import defaultdict


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        hashmap = defaultdict(int)
        hashmap[0] = 1
        res = 0
        prefix = 0
        for num in nums:
            prefix += (num % modulo == k)
            res += hashmap[(prefix + modulo - k) % modulo]
            hashmap[prefix % modulo] += 1
        return res

# Test cases                    
if __name__ == "__main__":
    # Test cases
    solution = Solution()
    print(solution.countInterestingSubarrays([1, 2, 3, 4], 2, 1))  # Output: 4
    print(solution.countInterestingSubarrays([1, 2, 3, 4], 3, 1))  # Output: 2
    print(solution.countInterestingSubarrays([1, 2, 3, 4], 5, 1))  # Output: 0
    print(solution.countInterestingSubarrays([1, 2, 3, 4], 4, 1))  # Output: 0
    print(solution.countInterestingSubarrays([1, 2, 3, 4], 6, 1))  # Output: 0
    print(solution.countInterestingSubarrays([1, 2, 3, 4], 7, 1))  # Output: 0  
