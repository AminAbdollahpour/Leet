from typing import List


class Solution:
    def minimum_path(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        result = [[float('inf')] * (cols + 1) for r in range(rows + 1)]
        result[rows - 1][cols] = 0
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                result[i][j] = grid[i][j] + min(result[i + 1][j], result[i][j + 1])
        return result[0][0]
