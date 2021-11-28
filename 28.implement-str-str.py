#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, a: str, b: str) -> int:
        if len(a) == 0 or len(b) == 0:
            return 0
        for i in range(len(a)):
            if i+len(b) >= len(a):
                break
            if a[i:i+len(b)] == b:
                return i
        return -1
# @lc code=end

