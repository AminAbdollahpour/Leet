from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        goal = len(nums) - 1
        for i in reversed(range(len(nums) - 1)):
            print(i)
            print(goal)
            if i + nums[i] >= goal:
                if i == 0:
                    return True
                goal = i

        return False


s = Solution()
print(s.canJump(nums=[1]))
