from typing import List


class Solution:
    def climb_stairs(self, n: int) -> int:
        i = 0
        results = [1, 2]

        while i <= n:
            if n <= len(results):
                return results[n - 1]
            temp = results[i] + results[i + 1]
            results.append(temp)
            i += 1


