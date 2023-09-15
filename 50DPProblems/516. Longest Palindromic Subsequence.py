class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text2 = s[::-1]
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(s) + 1)]
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(s) - 1, -1, -1):
                if s[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]


