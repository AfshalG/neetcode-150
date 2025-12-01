"""
Problem: Two Sum
Difficulty: Easy
URL: https://leetcode.com/problems/two-sum/
Category: Arrays and Hashing

Description:
Given an array of integers nums and an integer target, return the indices i and j 
such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that 
satisfy the condition. Return the answer with the smaller index first.

Approach:
Use a hash map to store numbers we've seen along with their indices. For each
number, calculate the difference (target - num). If this difference exists in
our hash map, we've found our pair. Otherwise, store the current number and its
index in the hash map and continue. This allows us to find the pair in a single
pass through the array.

Time Complexity: O(n) - where n is the size of the input array
Space Complexity: O(n) - to store elements in the hash map

Date: 1 December 2025
Attempts: Solved
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array_index = {}  # stores number -> its index

        for i, num in enumerate(nums):
            diff = target - num

            if diff in array_index:
                return [array_index[diff], i]

            array_index[num] = i

        return []


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums = [3, 4, 5, 6]
    target = 7
    result = solution.twoSum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Expected: [0, 1]")
    print(f"Explanation: nums[0] + nums[1] == 7")
    print()
    
    # Test case 2
    nums = [4, 5, 6]
    target = 10
    result = solution.twoSum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Expected: [0, 2]")
    print()
    
    # Test case 3
    nums = [5, 5]
    target = 10
    result = solution.twoSum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Expected: [0, 1]")
