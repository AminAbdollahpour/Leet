from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            Sum = numbers[l] + numbers[r]
            if Sum < target:
                l += 1
            elif Sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]

s = Solution()
print(s.twoSum(numbers = [2,7,11,15], target = 9))