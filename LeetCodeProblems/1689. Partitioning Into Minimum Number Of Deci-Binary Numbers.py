class Solution:
    def minPartitions(self, n: str) -> int:
        maxDigit = 0
        for i in range(len(n)):
            maxDigit = max(maxDigit, int(n[i]))
        return maxDigit

