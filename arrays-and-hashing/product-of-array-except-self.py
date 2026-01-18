"""
Problem: Product of Array Except Self
Difficulty: Medium
URL: https://leetcode.com/problems/product-of-array-except-self/
Category: Arrays and Hashing

Description:
Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i]. You must write an
algorithm that runs in O(n) time and without using the division operation.

Approach:
Use two passes: first calculate the prefix products (product of all elements before i),
then calculate the postfix products (product of all elements after i). Multiply them
together to get the result. We can optimize space by storing prefix in the result array
and calculating postfix on the fly.

Time Complexity: O(n) - where n is the size of the input array
Space Complexity: O(1) - not counting the output array

Date: [Date Solved]
Attempts: [Number of attempts]
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums = [1, 2, 3, 4]
    result = solution.productExceptSelf(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}")
    print(f"Expected: [24, 12, 8, 6]")
    print()

    # Test case 2
    nums = [-1, 1, 0, -3, 3]
    result = solution.productExceptSelf(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}")
    print(f"Expected: [0, 0, 9, 0, 0]")
