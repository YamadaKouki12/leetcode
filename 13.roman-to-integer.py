# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        s.replace('IV','IIII').replace('IX','VIIII')
        s.replace('XL','XXXX').replace('XC','LXXXX')
        s.replace('CD','CCCC').replace('CM','DCCCC')
        print(s)
        for c in s:
            res += roman[c]
        return res

# @lc code=end