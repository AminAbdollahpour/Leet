from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        lenF = len(flowerbed)
        flowerbed.append(0)
        flowerbed.insert(0, 0)
        temp = 0
        for i in range(1, lenF + 1):
            if flowerbed[i] != 1 and flowerbed[i + 1] != 1 and flowerbed[i - 1] != 1:
                temp += 1
                flowerbed[i] = 1
        if temp >= n:
            return True
        return False


