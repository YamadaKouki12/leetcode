#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        max = strs[0]
        index = 0
        n = len(strs)
        for i in range(1,n):
            if len(strs[i])>len(max):
                max = strs[i]
                index = i

        res = ''
        for i in range(1,len(strs[index])+1):
            sub = strs[index][0:i]
            can = True
            for j in range(n):
                if j==index:
                    continue
                if strs[j][0:len(sub)] != sub:
                    can = False
                    break
            if can and len(res)<len(sub):
                res = sub
        return res

# @lc code=end

