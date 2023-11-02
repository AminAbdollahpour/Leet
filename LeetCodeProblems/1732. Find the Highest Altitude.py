from typing import List


class Solution:
        def largestAltitude(self, gain: List[int]) -> int:
            altitude = [0]
            for i in range(len(gain)):
                altitude.append(sum(gain[:i+1]))
            return max(altitude)


