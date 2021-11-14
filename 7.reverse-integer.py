#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if len(s)==1:
            return s
        elif x>0:
            s=s[::-1]
            ans = ''
            zero = True
            for i in range(len(s)):
                if zero and s[i]=='0':
                    pass
                else:
                    ans += s[i]
                if s[i] != '0':
                    zero = False
            num = int(s)
            if num > 2**31-2:
                return 0
            else:
                return ans
        else:
            s=s[1:]
            s=s[::-1]
            ans = ''
            zero = True
            for i in range(len(s)):
                if zero and s[i]=='0':
                    pass
                else:
                    ans += s[i]
                if s[i] != '0':
                    zero = False
            num = int(s)
            if num > 2**31-1:
                return 0
            else:
                return '-'+ans
# @lc code=end

