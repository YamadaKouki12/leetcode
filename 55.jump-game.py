#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1,n):
            if dp[i-1] < i:
                return False
            else:
                dp[i] = max(dp[i-1], i+nums[i])
            if dp[i] >= n-1:
                return True
        return dp[n-2] >= n-1
# @lc code=end

