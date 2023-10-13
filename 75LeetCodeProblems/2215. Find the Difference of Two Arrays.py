from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[], []]
        for number in nums1:
            if number not in nums2:
                if number not in answer[0]:
                    answer[0].append(number)
        for number in nums2:
            if number not in nums1:
                if number not in answer[1]:
                    answer[1].append(number)
        return answer


s = Solution()
print(s.findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))
