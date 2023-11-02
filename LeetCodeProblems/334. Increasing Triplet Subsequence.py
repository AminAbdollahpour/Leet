from math import inf
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first , second = inf , inf
        for third in nums:
            if second < third:
                return True
            if third <= first:
                first = third
            else:
                second = third
        return False
