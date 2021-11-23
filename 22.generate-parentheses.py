#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        for bit in range(1<<(n*2)):
            s = ''
            for i in range(n*2):
                if bit & (1<<i):
                    s+=')'
                else:
                    s+='('
            res.append(s)
        return res
# @lc code=end

