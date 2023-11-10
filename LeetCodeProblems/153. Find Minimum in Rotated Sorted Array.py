from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            else:
                pivot = arr[0]
                left = [x for x in arr[1:] if x < pivot]
                right = [x for x in arr[1:] if x >= pivot]
                return quick_sort(left) + [pivot] + quick_sort(right)

        return quick_sort(nums)[0]


