from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans = []
        for i in range(len(heights)):
            max_index = heights.index(max(heights))
            heights[max_index] = 0
            ans.append(names[max_index])
        return ans
