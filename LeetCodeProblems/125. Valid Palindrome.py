import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = re.sub(r'\W+', '', s).lower().replace('_','')
        print(newS)
        if newS == newS[::-1]:
            return True

        return False


