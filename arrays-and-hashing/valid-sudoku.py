"""
Problem: Valid Sudoku
Difficulty: Medium
URL: https://leetcode.com/problems/valid-sudoku/
Category: Arrays and Hashing

Description:
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated
according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition.

Approach:
Use hash sets to track seen numbers in each row, column, and 3x3 sub-box. For each
cell, check if the number already exists in its corresponding row, column, or box set.
The box index can be calculated using (r // 3, c // 3).

Time Complexity: O(1) - since the board is always 9x9
Space Complexity: O(1) - fixed size hash sets

Date: [Date Solved]
Attempts: [Number of attempts]
"""

from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1 - Valid Sudoku
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    result = solution.isValidSudoku(board)
    print(f"Output: {result}")
    print(f"Expected: True")
    print()

    # Test case 2 - Invalid Sudoku (duplicate in row)
    board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    result = solution.isValidSudoku(board)
    print(f"Output: {result}")
    print(f"Expected: False")
