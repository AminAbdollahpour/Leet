from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        left = 0
        right = len(nums)-1
        nums.sort()
        while left<right:
            sum = nums[left]+nums[right]
            if sum>k:
                right-=1
            elif sum<k:
                left+=1
            else:
                counter+=1
                right-=1
                left+=1
        return counter







s = Solution()
print(s.maxOperations(nums = [1,2,3,4], k = 5))
