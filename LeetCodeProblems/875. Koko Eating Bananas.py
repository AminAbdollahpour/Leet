import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right
        while left <= right:
            k = (left + right) // 2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile/k)
            if hour <= h:
                ans = min(ans,k)
                right = k-1
            else:
                left = k+1
        return ans
