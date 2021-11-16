#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            s,e = i+1,n-1
            while s < e:
                sum = nums[i]+nums[s]+nums[e]
                if sum == 0:
                    res.append([nums[i],nums[s],nums[e]])
                    while s<e and nums[s]==nums[s+1]: s+=1
                    while s<e and nums[e]==nums[e-1]: e-=1
                    s+=1
                    e-=1
                elif sum < 0:
                    s+=1
                else:
                    e-=1
        return res

# @lc code=end