#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [10**5] * n
        dp[0] = 0
        for i in range(n):
            for j in range(i+1,min(i+nums[i]+1,n)):
                dp[j] = min(dp[j], dp[i]+1)
        print(dp)
        return dp[n-1]
# @lc code=end


