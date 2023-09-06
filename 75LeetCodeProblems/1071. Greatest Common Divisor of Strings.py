class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def validate(i):
            if len1 % i or len2 % i:
                return False
            f1, f2 = len1 // i, len2 // i
            return str1[:i] * f1 == str1 and str1[:i] * f2 == str2

        for i in range(min(len1, len2), 0, -1):
            if validate(i):
                return str1[:i]
        return ""


s = Solution()
print(s.gcdOfStrings(str1="TAUXXTAUXXTAUXXTAUXXTAUXX", str2="TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
