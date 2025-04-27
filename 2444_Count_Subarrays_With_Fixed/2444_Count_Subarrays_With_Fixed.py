"""
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
Example 2:

Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

"""

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
         # Initialize pointers for tracking the positions of min_k, max_k, and out-of-range elements
        last_min_k = last_max_k = last_out_of_range = -1
      
        # Initialize the counter for the valid subarrays
        valid_subarrays_count = 0
      
        # Iterate through the list, checking each number against min_k and max_k
        for index, value in enumerate(nums):
            # Invalidate the subarray if the value is out of the specified range
            if value < minK or value > maxK:
                last_out_of_range = index

            # Update the last seen index for min_k, if found
            if value == minK:
                last_min_k = index

            # Update the last seen index for max_k, if found
            if value == maxK:
                last_max_k = index
          
            # Add to the count the number of valid subarrays ending with the current element
            # which is determined by the smallest index among last_min_k and last_max_k after the 
            # last out-of-range element
            valid_subarrays_count += max(0, min(last_min_k, last_max_k) - last_out_of_range)
      
        # Return the total count of valid subarrays
        return valid_subarrays_count
# Test cases
if __name__ == "__main__":
    # Test cases
    solution = Solution()
    print(solution.countSubarrays([1, 3, 5, 2, 7, 5], 1, 5))  # Output: 2
    print(solution.countSubarrays([1, 1, 1, 1], 1, 1))        # Output: 10
    print(solution.countSubarrays([1, 2, 3, 4], 2, 4))        # Output: 0
    print(solution.countSubarrays([1, 2, 3, 4], -1, -1))      # Output: 0
    print(solution.countSubarrays([5, 6, 7], 5, 7))           # Output: 3
    print(solution.countSubarrays([1, 2, 3, 4], 1, 4))        # Output: 0
    print(solution.countSubarrays([1, 2, 3, 4], 0, 5))        # Output: 0