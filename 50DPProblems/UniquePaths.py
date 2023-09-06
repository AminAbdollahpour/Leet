import math


class Solution:
    def unique_paths(self, m: int, n: int) -> int:
        top = (m - 1) + (n - 1)
        minNum = min(m - 1, n - 1)
        down = math.factorial(minNum) * math.factorial(top - minNum)
        return int(math.factorial(top) / down)
        #test
