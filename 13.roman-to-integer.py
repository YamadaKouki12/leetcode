#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        s = s + '.'
        ans = 0
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, '.':0}
        for i in range(len(s)):
            if((s[i]=='I' or s[i]=='X' or s[i]=='C') and s[i]!=s[i+1]):
                ans += (dic[s[i+1]]-dic[s[i]])
            else:
                ans += dic[s[i]]
        return ans


# @lc code=end

