#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def dfs(self, res: List[List[int]],now: List[int], lis: List[int], target: int, before: int) -> bool:
        if target == 0:
            res.append(now)
            return True
        for i in range(before, len(lis)):
            if target - lis[i] < 0:
                return False
            self.dfs(res,now+[lis[i]], lis,target-lis[i], i)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(res,[], sorted(candidates), target, 0)
        return res
# @lc code=end