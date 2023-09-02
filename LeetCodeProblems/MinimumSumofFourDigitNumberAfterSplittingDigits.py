class Solution:
    def minimum_sum(self, num: int) -> int:
        nums = sorted(str(num))
        return int(nums[0]+nums[2])+int(nums[1]+nums[3])
