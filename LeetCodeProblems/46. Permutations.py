from typing import List
import math


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)

            permutation = self.permute(nums)
            for perm in permutation:
                perm.append(n)
            result.extend(permutation)
            nums.append(n)
        return result
