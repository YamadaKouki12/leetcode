#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        res, cnt, size = [], 0, len(mat) * len(mat[0])
        n,e,s,w = 0, len(mat[0])-1, len(mat)-1, 0
        while True:
            for i in range(w,e+1):
                res.append(mat[n][i])
                cnt += 1
            n += 1
            if cnt >= size: break
            for i in range(n,s+1):
                res.append(mat[i][e])
                cnt += 1
            e -= 1
            if cnt >= size: break
            for i in range(e,w-1,-1):
                res.append(mat[s][i])
                cnt += 1
            s -= 1
            if cnt >= size: break
            for i in range(s,n-1,-1):
                res.append(mat[i][w])
                cnt += 1
            w += 1
            if cnt >= size: break
        print(f'n={n},e={e},s={s},w={w}')
        print(res)
        return res
# @lc code=end