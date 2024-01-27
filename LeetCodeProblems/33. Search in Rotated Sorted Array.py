from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def sorter(arr: List[int]) -> List:
            index = arr.index(min(arr))
            return arr[index:] + arr[:index]

        def binary_search(list, target):
            low = 0
            high = len(list) - 1

            while low <= high:
                mid = (low + high) // 2

                if list[mid] == target:
                    return mid
                elif list[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return -1

        srted = sorter(nums)
        return binary_search(srted, target)
