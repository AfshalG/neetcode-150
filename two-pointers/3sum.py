"""
Problem: 3Sum
Difficulty: Medium
URL: https://leetcode.com/problems/3sum/
Category: Two Pointers

Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
The solution set must not contain duplicate triplets.

Approach:
Sort the array first. For each element, use two pointers to find pairs that sum
to the negative of that element. Skip duplicates to avoid duplicate triplets.
Sort ensures we can use two pointers efficiently and handle duplicates.

Time Complexity: O(n²) - where n is the length of the array
Space Complexity: O(1) or O(n) - depending on sorting implementation

Date: [Date Solved]
Attempts: [Number of attempts]
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums = [-1, 0, 1, 2, -1, -4]
    result = solution.threeSum(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}")
    print(f"Expected: [[-1, -1, 2], [-1, 0, 1]]")
    print()

    # Test case 2
    nums = [0, 1, 1]
    result = solution.threeSum(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}")
    print(f"Expected: []")
    print()

    # Test case 3
    nums = [0, 0, 0]
    result = solution.threeSum(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}")
    print(f"Expected: [[0, 0, 0]]")
