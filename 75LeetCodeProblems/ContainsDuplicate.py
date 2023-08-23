from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for index in range(len(nums) - 1):
            if index == len(nums):
                return False
            elif nums[index] == nums[index + 1]:
                return True
        return False
