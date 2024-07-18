from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        op = 0
        for i in range(len(nums)):
            if nums[i] % 3 == 0:
                continue
            else:
                if 3 / nums[i] > 0.5:
                    nums[i] -= 1
                    op += 1
                    i -= 1
                else:
                    nums[i] += 1
                    op += 1
                    i -= 1
        return op