class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    return self.isSubsequence(s[i + 1:], t[j + 1:])
                elif s[i] != t[j] and j == len(t)-1:
                    return False


