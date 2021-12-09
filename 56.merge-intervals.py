#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        res: List[List[int]] = [intervals[0]]
        for i in range(1,n):
            last = res.pop()
            if last[1] >= intervals[i][0]:
                res.append([last[0],max(last[1],intervals[i][1])])
            else:
                res.append(last)
                res.append(intervals[i])
        return(res)
# @lc code=end

