"""
Problem: Two Sum II - Input Array Is Sorted
Difficulty: Medium
URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Category: Two Pointers

Description:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing
order, find two numbers such that they add up to a specific target number. Return
the indices of the two numbers (1-indexed) as an integer array [index1, index2].

Approach:
Use two pointers, one at the start and one at the end. Calculate the sum of the
two numbers. If sum is too small, move left pointer right. If sum is too large,
move right pointer left. Continue until we find the target sum.

Time Complexity: O(n) - where n is the length of the array
Space Complexity: O(1) - only using pointers

Date: [Date Solved]
Attempts: [Number of attempts]
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

        return []


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    numbers = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(numbers, target)
    print(f"Input: numbers = {numbers}, target = {target}")
    print(f"Output: {result}")
    print(f"Expected: [1, 2]")
    print()

    # Test case 2
    numbers = [2, 3, 4]
    target = 6
    result = solution.twoSum(numbers, target)
    print(f"Input: numbers = {numbers}, target = {target}")
    print(f"Output: {result}")
    print(f"Expected: [1, 3]")
    print()

    # Test case 3
    numbers = [-1, 0]
    target = -1
    result = solution.twoSum(numbers, target)
    print(f"Input: numbers = {numbers}, target = {target}")
    print(f"Output: {result}")
    print(f"Expected: [1, 2]")
