#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1,n):
            if dp[i-1]>0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i]  = nums[i]
            res = max(res, dp[i])
        return res
# @lc code=end

