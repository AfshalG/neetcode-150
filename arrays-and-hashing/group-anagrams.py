"""
Problem: Group Anagrams
Difficulty: Medium
URL: https://leetcode.com/problems/group-anagrams/
Category: Arrays and Hashing

Description:
Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.

Approach:
Use a hash map where the key is a tuple representing the character frequency count.
For each string, create a count array of size 26 (for 'a' to 'z') to track the
frequency of each character. Convert this array to a tuple (since lists can't be
hash keys) and use it as the key in our hash map. All anagrams will have the same
character frequency pattern and thus the same key, grouping them together.

Time Complexity: O(m * n) - where m is the number of strings and n is the length 
                            of the longest string
Space Complexity: O(m) - to store all strings in the hash map

Date: 2 December 2025
Attempts: Solved
"""

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(string)
        return list(res.values())


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    result = solution.groupAnagrams(strs)
    print(f"Input: strs = {strs}")
    print(f"Output: {result}")
    print(f"Expected: [['hat'], ['act', 'cat'], ['stop', 'pots', 'tops']]")
    print()
    
    # Test case 2
    strs = ["x"]
    result = solution.groupAnagrams(strs)
    print(f"Input: strs = {strs}")
    print(f"Output: {result}")
    print(f"Expected: [['x']]")
    print()
    
    # Test case 3
    strs = [""]
    result = solution.groupAnagrams(strs)
    print(f"Input: strs = {strs}")
    print(f"Output: {result}")
    print(f"Expected: [['']]")
