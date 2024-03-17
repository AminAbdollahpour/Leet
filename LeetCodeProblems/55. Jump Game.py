from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in reversed(range(len(nums) - 1)):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False
