#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#
import math
# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0 : return 0
        return (num-1)%9 + 1
# @lc code=end
