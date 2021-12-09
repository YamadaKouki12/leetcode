#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d = defaultdict(lambda:[])
        for str in strs:
            key = ''.join(sorted(str))
            d[key] += [str]
        return d.values()
        
        """
        n = len(strs)
        lis = []
        res = []
        for i in range(n):
            lis.append([''.join(sorted(strs[i])),i])
        lis.sort(key=lambda x: x[0])
        i = 0
        tmp = []
        while i<n-1:
            if lis[i][0] == lis[i+1][0]:
                tmp.append(strs[lis[i][1]])
            else:
                tmp.append(strs[lis[i][1]])
                res.append(tmp)
                tmp = []
            i += 1
        tmp.append(strs[lis[n-1][1]])
        res.append(tmp)
        return res
        """

# @lc code=end