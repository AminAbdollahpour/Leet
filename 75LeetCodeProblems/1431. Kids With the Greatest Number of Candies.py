from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candylen = len(candies)
        result = [False] * candylen
        maxCa = max(candies)
        for i in range(candylen):
            if candies[i] + extraCandies >= maxCa:
                result[i] = True
        return result
