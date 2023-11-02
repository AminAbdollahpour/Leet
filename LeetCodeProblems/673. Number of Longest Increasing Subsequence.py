from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}
        lenLIS, res = 0, 0
        for i in reversed(range(len(nums))):
            maxLen, maxCount = 1, 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length, count = dp[j]
                    if length + 1 > maxLen:
                        maxLen, maxCount = length + 1, count
                    elif length + 1 == maxLen:
                        maxCount += count
            if maxLen > lenLIS:
                lenLIS, res = maxLen, maxCount
            elif maxLen == lenLIS:
                res += maxCount

            dp[i] = [maxLen, maxCount]
        return res
