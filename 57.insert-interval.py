#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = [intervals[0]]
        for i in range(1,n):
            last = res.pop()
            if last[1] <= intervals[i][0]:
                

# @lc code=end

