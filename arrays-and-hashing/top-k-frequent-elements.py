"""
Problem: Top K Frequent Elements
Difficulty: Medium
URL: https://leetcode.com/problems/top-k-frequent-elements/
Category: Arrays and Hashing

Description:
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Approach:
Use a hash map to count the frequency of each element, then use bucket sort
to group elements by their frequency. Finally, collect the k most frequent
elements by iterating from the highest frequency bucket downwards.

Time Complexity: O(n) - where n is the size of the input array
Space Complexity: O(n) - for the hash map and frequency buckets

Date: [Date Solved]
Attempts: [Number of attempts]
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = solution.topKFrequent(nums, k)
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Output: {result}")
    print(f"Expected: [1, 2]")
    print()

    # Test case 2
    nums = [1]
    k = 1
    result = solution.topKFrequent(nums, k)
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Output: {result}")
    print(f"Expected: [1]")
