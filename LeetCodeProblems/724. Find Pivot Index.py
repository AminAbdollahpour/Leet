from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        if 0 == sum(nums[1:]):
            return 0

        for i in range(length - 1):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        if 0 == sum(nums[:length - 1]):
            return length - 1
        return -1
