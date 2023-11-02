from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        for i in range(len(nums)) :
            if nums[i] == 0:
                zeros.append(i)

        for index in reversed(zeros):
            del nums[index]

        for zero in zeros:
            nums.append(0)
