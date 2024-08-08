from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        setlist = set(nums)
        if len(nums) == len(setlist):
            return False
        return True
