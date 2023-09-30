from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for number in set(nums):
            if nums.count(number)>(len(nums)/2):
                return number