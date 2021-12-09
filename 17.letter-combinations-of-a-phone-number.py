#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
""" dfs
class Solution:
    def dfs(self,res, digits, dic, tmp, pointer):
        if pointer == len(digits):
            res.append(tmp)
            return True
        charas = dic[digits[pointer]]
        for c in charas:
            self.dfs(res, digits, dic, tmp+c, pointer+1)
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res: List[str] = []
        self.dfs(res, digits, dic, '', 0)
        return res
"""

""" bfs """
class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        from collections import deque
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res: List[str] = []
        q = deque()
        q.append(('',0))
        while q:
            tmp, pointer = q.pop()
            print(tmp,pointer)
            if pointer == len(digits):
                res.append(tmp)
                continue
            for c in dic[digits[pointer]]:
                q.append((tmp+c,pointer+1))
        return res

# @lc code=end≈