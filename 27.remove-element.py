#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n-1,-1,-1):
            if nums[i] == val:
                nums[i]=nums[n-1-ans]
                nums[n-1-ans] = -1
                ans += 1
        return n - ans

# @lc code=end

