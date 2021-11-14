#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = s[0]
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            ans = s[i]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    if j-i==1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        ans = ans if len(ans) > (j-i+1) else s[i:j+1]

        return ans

# @lc code=end

