#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, res, [], target, 0)
        return res
    def dfs(self, candidates: List[int], res: List[int], lis: List[int], target: int, now: int) -> bool:
        if target == 0:
            res.append(lis)
            return True
        for i in range(now,len(candidates)):
            if i > now and candidates[i] == candidates[i-1]:
                continue
            if target - candidates[i] < 0:
                return False
            self.dfs(candidates, res, lis+[candidates[i]], target-candidates[i], i+1)
# @lc code=end