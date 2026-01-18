"""
Problem: Valid Palindrome
Difficulty: Easy
URL: https://leetcode.com/problems/valid-palindrome/
Category: Two Pointers

Description:
Given a string s, return true if it is a palindrome, or false otherwise.
A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Approach:
Use two pointers, one at the start and one at the end. Skip non-alphanumeric characters
and compare characters case-insensitively. Move pointers inward until they meet.

Time Complexity: O(n) - where n is the length of the string
Space Complexity: O(1) - only using pointers

Date: [Date Solved]
Attempts: [Number of attempts]
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    s = "A man, a plan, a canal: Panama"
    result = solution.isPalindrome(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print(f"Expected: True")
    print()

    # Test case 2
    s = "race a car"
    result = solution.isPalindrome(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print(f"Expected: False")
    print()

    # Test case 3
    s = " "
    result = solution.isPalindrome(s)
    print(f"Input: '{s}'")
    print(f"Output: {result}")
    print(f"Expected: True")
