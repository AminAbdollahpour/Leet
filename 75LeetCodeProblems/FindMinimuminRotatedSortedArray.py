from typing import List


class Solution:
    def find_min(self, nums: List[int]) -> int:
        nums.sort()
        return nums[0]
