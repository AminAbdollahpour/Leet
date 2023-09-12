from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lens = []
        for word in wordDict:
            lens.append(len(word))
        for word in wordDict:
            if len(s) < min(lens):
                return False
            elif word == s[:len(word)]:
                return self.wordBreak(s[:len(word)], wordDict)



s = Solution()
print(s.wordBreak(s="leetcode", wordDict=["leet", "code"]))
