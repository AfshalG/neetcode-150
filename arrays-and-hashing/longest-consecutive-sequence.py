"""
Problem: Longest Consecutive Sequence
Difficulty: Medium
URL: https://leetcode.com/problems/longest-consecutive-sequence/
Category: Arrays and Hashing

Description:
Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence. You must write an algorithm that runs in O(n) time.

Approach:
Convert the array to a set for O(1) lookups. For each number, check if it's the
start of a sequence (num - 1 not in set). If it is, count the length of the
consecutive sequence starting from that number. Track the maximum length found.

Time Complexity: O(n) - where n is the size of the input array
Space Complexity: O(n) - for the set

Date: [Date Solved]
Attempts: [Number of attempts]
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums = [100, 4, 200, 1, 3, 2]
    result = solution.longestConsecutive(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}")
    print(f"Expected: 4 (sequence: [1, 2, 3, 4])")
    print()

    # Test case 2
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    result = solution.longestConsecutive(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}")
    print(f"Expected: 9 (sequence: [0, 1, 2, 3, 4, 5, 6, 7, 8])")
