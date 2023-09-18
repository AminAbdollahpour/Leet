from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,n in enumerate(nums):
            dif = target - n
            if dif in dic:
                return [dic[dif],i]
            dic[n] = i
