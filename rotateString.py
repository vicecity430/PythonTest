#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(goal)):
            if s == (goal[0:i] + goal[i:]):
                return True
            rgoal = goal[::-1]
            if s == (rgoal[0:i] + rgoal[i:]):
                return True
        return False
# @lc code=end
