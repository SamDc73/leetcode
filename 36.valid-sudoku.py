'''
1. search through every row
2. search through every column
3. search through every square (3x3 squrare)
    1. key is (row // 3, columm // 3)
    2. value is a hash map
'''

import collections


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create hash set for rows, columns, squares
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (row / 3, col / 3)

        # because sudoko board is 9 X 9:
        for c in range(9):
            for r in range(9):
                if board[c][r] == '.':  # for empty cell they are using dot
                    continue
                if (
                    board[c][r] in cols[c]
                    or board[c][r] in rows[r]
                    or board[c][r] in squares[(c // 3, r // 3)]
                ):
                    return false
                cols[c].add(board[c][r])
                rows[r].add(board[c][r])
                squares[(c // 3, r // 3)].add(board[c][r])
        return true
