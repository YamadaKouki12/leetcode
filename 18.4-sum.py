#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n-3):
            for j in range(i+1,n-2):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                if nums[j]==nums[j-1] and nums[j]!=nums[i]:
                # if j<n-3 and nums[j]==nums[j+1]:
                    continue
                k,l = j+1,n-1
                while k<l:
                    sum = nums[i]+nums[j]+nums[k]+nums[l]
                    if sum == target:
                        res.append((nums[i],nums[j],nums[k],nums[l]))
                        # print(f'[{i},{j},{k},{l}]')
                        while k<l and nums[k]==nums[k+1]:
                            k += 1
                        while k<l and nums[l]==nums[l-1]:
                            l -= 1
                        k += 1
                        l -= 1
                    elif sum < target:
                        k += 1
                    else:
                        l -= 1
        return set(res)
# @lc code=end

