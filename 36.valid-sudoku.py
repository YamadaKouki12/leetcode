#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        for i in range(n):
            lis: str = []
            for j in range(n):
                if board[i][j] in lis:
                    return False
                if board[i][j] != '.':
                    lis.append(board[i][j])

        for j in range(n):
            lis: str = []
            for i in range(n):
                if board[i][j] in lis:
                    return False
                if board[i][j] != '.':
                    lis.append(board[i][j])

        for i in range(0,9,3):
            for j in range(0,9,3):
                lis: str = []
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if board[k][l] in lis:
                            return False
                        if board[k][l] != '.':
                            lis.append(board[k][l])

        return True
# @lc code=end