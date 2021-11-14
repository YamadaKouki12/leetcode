#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) == 0:
            return 0
        ans = ''
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else:
            sign = 1
        for i in range(len(s)):
            if '0'<= s[i] <='9':
                ans += s[i]
            else:
                break
        if len(ans) == 0:
            return 0
        else:
            res = int(ans)
            if res >= 2**31 and sign==1:
                res = 2**31-1
            elif res > 2**31 and sign==-1:
                res = 2**31
            return res*sign

# @lc code=end

