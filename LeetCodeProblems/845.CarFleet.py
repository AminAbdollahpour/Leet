from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_to_destination = []
        n = len(position)
        for i in range(n):
            time_to_destination.append((target - position[i]) / speed[i])
        for j in range(n):
            for k in range(n):
                if (position[j] < position[k]) and (time_to_destination[j] < time_to_destination[k]):
                    time_to_destination[j] = time_to_destination[k]
        return len(set(time_to_destination))


s = Solution()
print(s.carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
