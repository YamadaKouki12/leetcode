#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def dfs(self,res, path, nums):
        if len(nums) == 0:
            res.append(path)
            return True
        for i in range(len(nums)):
            self.dfs(res,path+[nums[i]], nums[:i]+nums[i+1:])
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            self.dfs(res, [nums[i]], nums[:i]+nums[i+1:])
        return res
# @lc code=end

