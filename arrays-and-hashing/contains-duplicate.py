"""
Problem: Contains Duplicate
Difficulty: Easy
URL: https://leetcode.com/problems/contains-duplicate/
Category: Arrays and Hashing

Description:
Given an integer array nums, return true if any value appears more than once 
in the array, otherwise return false.

Approach:
Use a hash set to track elements we've seen. As we iterate through the array,
check if the current element is already in the set. If it is, we've found a
duplicate. If not, add it to the set and continue. This allows us to check
for duplicates in O(1) time per element.

Time Complexity: O(n) - where n is the size of the input array
Space Complexity: O(n) - in worst case, we store all unique elements

Date: 1 December 2025
Attempts: Solved
"""

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums = [1, 2, 3, 3]
    result = solution.hasDuplicate(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}")
    print(f"Expected: True")
    print()
    
    # Test case 2
    nums = [1, 2, 3, 4]
    result = solution.hasDuplicate(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}")
    print(f"Expected: False")