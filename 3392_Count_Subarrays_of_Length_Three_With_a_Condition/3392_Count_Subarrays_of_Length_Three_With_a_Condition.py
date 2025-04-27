"""
Given an integer array nums, return the number of subarrays of length 3 such that the sum of the first and third numbers equals exactly half of the second number.

Example 1:

Input: nums = [1,2,1,4,1]

Output: 1

Explanation:

Only the subarray [1,4,1] contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.

Example 2:

Input: nums = [1,1,1]

Output: 0

Explanation:

[1,1,1] is the only subarray of length 3. However, its first and third numbers do not add to half the middle number.


"""
from typing import List

def countSubarrays( nums: List[int]) -> int:
    n =len(nums)
    ans = 0
    for i in range(n-2):
        a = nums[i]
        b = nums[i+1]
        c = nums[i+2]
        if a+c == b/2:
            ans +=1
    return ans


# Test cases
if __name__ == "__main__":
    # Test cases
    print(countSubarrays([1, 2, 1, 4, 1]))  # Output: 1
    print(countSubarrays([1, 1, 1]))        # Output: 0
    print(countSubarrays([2, 4, 2]))        # Output: 0
    print(countSubarrays([3, 6, 3]))        # Output: 0
    print(countSubarrays([5, 10, 5]))       # Output: 0 
    print(countSubarrays([1, 2, 3, 4, 5]))  # Output: 0
