#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = n*(n+1)//2
        diff = s - sum(set(nums))
        err = sum(nums)+diff-s
        return [err,diff]
# @lc code=end

