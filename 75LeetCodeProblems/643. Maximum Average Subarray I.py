from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum = 0
        if len(nums) <= k:
            return sum(nums) / k
        else:
            for i in range(len(nums) - (k-1)):
                currentMax = sum(nums[i:k+i]) / k
                maximum = max(maximum, currentMax)
        return maximum


s = Solution()
print(s.findMaxAverage(nums = [0,1,1,3,3], k = 4))
