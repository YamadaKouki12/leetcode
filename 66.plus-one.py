#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n, carry = len(digits), 1
        for i in range(n-1, 0, -1):
            if digits[i] + carry == 10:
                digits[i] = 0
            else:
                digits[i] += carry
                carry = 0
        if digits[0] + carry == 10:
            digits[0] = 0
            digits.insert(0,1)
        else:
            digits[0] += carry
        return digits


# @lc code=end

