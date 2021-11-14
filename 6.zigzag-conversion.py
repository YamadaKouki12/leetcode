#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1:
            return s
        zig = [[' ']*n for _ in range(numRows)]
        cnt = 0
        for i in range(n):
            if i%(numRows-1) == 0:
                for j in range(numRows):
                    zig[j][i]=s[cnt]
                    cnt+=1
                    if cnt == len(s):
                        break
            else:
                zig[numRows-1-i%(numRows-1)][i]=s[cnt]
                cnt+=1
            if cnt == len(s):
                ans = ''
                # print(zig)
                for i in range(numRows):
                    for j in range(n):
                        if(zig[i][j]!=' '):
                            ans += zig[i][j]
                return ans
# @lc code=end

