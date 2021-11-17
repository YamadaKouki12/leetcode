#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits)==0:
            return []
        if len(digits)==1:
            return list(dic[digits[0]])
        lists = []
        for c in digits:
            lists.append([dic[c]])
        for list in lists:
            pass
# @lc code=end