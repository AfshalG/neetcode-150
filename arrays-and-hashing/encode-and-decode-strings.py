"""
Problem: Encode and Decode Strings
Difficulty: Medium
URL: https://leetcode.com/problems/encode-and-decode-strings/
Category: Arrays and Hashing

Description:
Design an algorithm to encode a list of strings to a single string and decode
that string back to the original list of strings.

Approach:
Use a length-based delimiter. For each string, prepend its length followed by a
delimiter (e.g., "#"). During decoding, read the length, skip the delimiter, and
extract the exact number of characters. This handles special characters and empty strings.

Time Complexity: O(n) - where n is the total length of all strings
Space Complexity: O(n) - for the encoded string

Date: [Date Solved]
Attempts: [Number of attempts]
"""

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    strs = ["neet", "code", "love", "you"]
    encoded = solution.encode(strs)
    decoded = solution.decode(encoded)
    print(f"Input: {strs}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    print(f"Match: {strs == decoded}")
    print()

    # Test case 2
    strs = ["we", "say", ":", "yes"]
    encoded = solution.encode(strs)
    decoded = solution.decode(encoded)
    print(f"Input: {strs}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    print(f"Match: {strs == decoded}")
