#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1,-1]
        left, right = self.search_left(nums, target), self.search_right(nums, target)
        left = self.search_left(nums, target)
        print(left, right)
        if left>=n or nums[left] != target:
            return [-1,-1]
        return [left, right-1]

    def search_left(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ng, ok = -1, n
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if nums[mid] >= target:
                ok = mid
            else:
                ng = mid
        return ok

    def search_right(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ng, ok = -1, n
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if nums[mid] > target:
                ok = mid
            else:
                ng = mid
        return ok
# @lc code=end