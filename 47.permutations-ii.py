#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def dfs(self,res, path, nums):
        if len(nums) == 0:
            res.append(path)
            return True
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            self.dfs(res,path+[nums[i]], nums[:i]+nums[i+1:])
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            self.dfs(res, [nums[i]], nums[:i]+nums[i+1:])
        return res
# @lc code=end

