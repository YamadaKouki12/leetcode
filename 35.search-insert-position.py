#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ng, ok = 0, len(nums)
        while(abs(ok-ng)>1):
            mid = (ng + ok) // 2
            if target <= nums[mid]:
                ok = mid
            else:
                ng = mid
        return ok
# @lc code=end

