from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        result = 1
        new = sorted(nums)
        if not nums:
            return 0
        for i in range(len(nums) - 1):
            if new[i + 1] == new[i] + 1:
                count += 1
            elif new[i + 1] == new[i]:
                continue
            elif new[i + 1] != new[i] + 1:
                result = max(result , count)
                count = 1
        return max(result , count)
