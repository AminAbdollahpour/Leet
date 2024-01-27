from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(arr: List[int]) -> int:
            left = 0
            right = len(arr) - 1
            mid = (left + right) // 2
            while left <= right:
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        up = binary_search(nums[min(nums):])
        down = binary_search(nums[:min(nums)])
        if up and down == -1:
            return -1
        elif up != -1:
            return up


s = Solution()
print(s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
