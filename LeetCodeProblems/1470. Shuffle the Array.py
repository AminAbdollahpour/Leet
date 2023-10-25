from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])

        return result
s = Solution()
print(s.shuffle(nums = [2,5,1,3,4,7], n = 3))
