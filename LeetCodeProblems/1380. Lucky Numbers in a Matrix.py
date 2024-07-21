from typing import List
import numpy as np


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows , columns = len(matrix) , len(matrix[0])
        lucky_numbers = []

        minimum = set()
        for row in range(rows):
            minimum.add(min(matrix[row]))

        maximum = set()
        for column in range(columns):
            current_max = matrix[0][column]
            for row in range(rows):
                current_max = max(current_max , matrix[row][column])
            maximum.add(current_max)

        for number in minimum:
            if number in maximum:
                lucky_numbers.append(number)

        return lucky_numbers


s = Solution()
print(s.luckyNumbers(matrix=[[7, 8], [1, 2]]))
