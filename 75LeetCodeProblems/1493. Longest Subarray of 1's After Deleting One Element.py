from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result = 0

        def longest_ones(arr):
            current_count = 0
            max_count = 0
            for number in arr:
                if number == 1:
                    current_count += 1
                    max_count = max(max_count, current_count)
                elif number == 0:
                    current_count = 0
            return max_count

        for i in range(len(nums)):
            result = max(longest_ones(nums[:i] + nums[i + 1:]), result)
        return result


s = Solution()
print(s.longestSubarray(nums = [1,1,1]))
