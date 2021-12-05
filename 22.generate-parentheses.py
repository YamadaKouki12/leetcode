#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
""" solution by dfs
class Solution:
    def dfs(self, res: List[str], lis: str, cnt: int, n: int):
        if len(lis) == n*2 and cnt == n:
            res.append(lis)
            return True
        if cnt < n:
            self.dfs(res,lis+'(', cnt+1, n)
        if cnt > len(lis)-cnt:
            self.dfs(res,lis+')', cnt, n)

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(res,'(',1, n)
        return res
"""

""" solution by dfs """
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        from collections import deque
        q = deque()
        q.append(('(', 1, 0))
        res = []
        while q:
            s, l, r = q.pop()
            if l+r==n*2:
                res.append(s)
                continue
            if l < n:
                q.append((s+'(', l+1, r))
            if l>r:
                q.append((s+')', l, r+1))
        return res

# @lc code=end

