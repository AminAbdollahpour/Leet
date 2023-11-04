from typing import List


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        sum = 0
        for number in nums:
            sum += number
            if sum > maxsum:
                maxsum = sum
            if sum < 0:
                sum = 0
        return maxsum
