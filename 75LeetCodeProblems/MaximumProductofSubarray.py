from typing import List


class Solution:
    def max_product(self, nums: List[int]) -> int:
        result = max(nums)
        currentMax , currentMin = 1 , 1
        for number in nums:
            temp = currentMax * number
            currentMax = max(currentMax * number , currentMin * number , number)
            currentMin = min(temp , currentMin * number , number)
            result = max(result , currentMax)
        return result