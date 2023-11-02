from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]):
        matrix.append([2**31] * len(matrix[0]))
        for righ_row in matrix:
            righ_row.append(2**31)
            righ_row.insert(0, 2**31)
        for i in range(len(matrix) - 3, -1, -1):
            for j in range(1, len(matrix[0]) - 1):
                matrix[i][j] = min(matrix[i][j] + matrix[i + 1][j], matrix[i][j] + matrix[i + 1][j + 1],
                                   matrix[i][j] + matrix[i + 1][j - 1])
        result = float('inf')
        matrix[0].pop(0)
        for i in range(len(matrix[0]) - 1):
            result = min(result, matrix[0][i])
        return result

