#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mapping = {'(':')','{':'}','[':']'}
        n = len(s)
        if n%2 != 0:
            return False
        for c in s:
            if c=='(' or c=='[' or c=='{':
                st.append(c)
            else:
                if len(st)==0 or c!=mapping[st[-1]]:
                    return False
                else:
                    st.pop()
        if len(st) == 0:
            return True
        else:
            return False
# @lc code=end

