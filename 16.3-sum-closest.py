#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = 10**4
        for i in range(n-2):
            j,k =i+1, n-1
            while j<k:
                sum = nums[i]+nums[j]+nums[k]
                res = sum if abs(target-sum)<abs(target-res) else res
                if sum == target:
                    return sum
                elif sum > target:
                    k-=1
                else:
                    j+=1
        return res


# @lc code=end