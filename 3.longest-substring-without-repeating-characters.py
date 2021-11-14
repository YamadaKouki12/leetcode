#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        start = 0
        used = {}
        for i,c in enumerate(s):
            if c in used and used[c]>=start:
                start = used[c] + 1
            used[c] = i
            ans = max(ans, i-start+1)
        return ans
# @lc code=end