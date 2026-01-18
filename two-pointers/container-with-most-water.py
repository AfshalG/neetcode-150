"""
Problem: Container With Most Water
Difficulty: Medium
URL: https://leetcode.com/problems/container-with-most-water/
Category: Two Pointers

Description:
You are given an integer array height of length n. There are n vertical lines drawn
such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find
two lines that together with the x-axis form a container that contains the most water.
Return the maximum amount of water a container can store.

Approach:
Use two pointers starting at both ends. Calculate the area formed by the two lines
and track the maximum. Move the pointer pointing to the shorter line inward, as
moving the taller line won't increase the area (width decreases and height is limited
by the shorter line).

Time Complexity: O(n) - where n is the length of the array
Space Complexity: O(1) - only using pointers

Date: [Date Solved]
Attempts: [Number of attempts]
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = solution.maxArea(height)
    print(f"Input: {height}")
    print(f"Output: {result}")
    print(f"Expected: 49")
    print()

    # Test case 2
    height = [1, 1]
    result = solution.maxArea(height)
    print(f"Input: {height}")
    print(f"Output: {result}")
    print(f"Expected: 1")
