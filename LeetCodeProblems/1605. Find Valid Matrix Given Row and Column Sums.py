from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        row, column = len(rowSum), len(colSum)
        ans = [[0] * column for _ in range(row)]
        for i in range(row):
            ans[i][0] = rowSum[i]
        for j in range(column):
            cur_sum = 0
            for r in range(row):
                cur_sum += ans[r][j]
            r = 0
            while cur_sum > colSum[j]:
                diff = cur_sum - colSum[j]
                shift = min(ans[r][j], diff)

                ans[r][j] -= shift
                ans[r][j + 1] += shift
                cur_sum -= shift
                r += 1
        return ans
