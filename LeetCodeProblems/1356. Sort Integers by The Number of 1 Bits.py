from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if str(bin(arr[i])).count('1') > str(bin(arr[j])).count('1'):
                    arr[i], arr[j] = arr[j], arr[i]
                elif str(bin(arr[i])).count('1') == str(bin(arr[j])).count('1'):
                    if arr[i] > arr[j]:
                        arr[i], arr[j] = arr[j], arr[i]

        return arr


s = Solution()
print(s.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
