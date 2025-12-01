"""
Problem: Valid Anagram
Difficulty: Easy
URL: https://leetcode.com/problems/valid-anagram/
Category: Arrays and Hashing

Description:
Given two strings s and t, return true if the two strings are anagrams of each 
other, otherwise return false. An anagram is a string that contains the exact 
same characters as another string, but the order of the characters can be different.

Approach:
Use two hash maps to count the frequency of each character in both strings.
If the lengths are different, they cannot be anagrams. Iterate through both
strings simultaneously, counting character frequencies in separate dictionaries.
Finally, compare the two dictionaries for equality.

Time Complexity: O(n + m) - where n and m are the lengths of strings s and t
Space Complexity: O(1) - at most 26 lowercase English letters

Date: 1 December 2025
Attempts: Solved
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1 
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT 


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    s = "racecar"
    t = "carrace"
    result = solution.isAnagram(s, t)
    print(f"Input: s = \"{s}\", t = \"{t}\"")
    print(f"Output: {result}")
    print(f"Expected: True")
    print()
    
    # Test case 2
    s = "jar"
    t = "jam"
    result = solution.isAnagram(s, t)
    print(f"Input: s = \"{s}\", t = \"{t}\"")
    print(f"Output: {result}")
    print(f"Expected: False")
