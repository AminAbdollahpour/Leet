from typing import List
import numpy as np


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        arr = np.array(matrix)
        lucky_numbers = []
        for i in range(len(matrix)):
            min_row = min(matrix[i])
            min_index = matrix[i].index(min_row)
            max_column = max(arr[:, min_index])
            if min_row >= max_column:
                lucky_numbers.append(min_row)

        return lucky_numbers


s = Solution()
print(s.luckyNumbers(matrix=[[7, 8], [1, 2]]))
