from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                for j in range(len(matrix[i])):
                    if matrix[i][j] == target:
                        return True
        return False
