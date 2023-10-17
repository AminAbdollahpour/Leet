class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        right = 1
        longest_palindromic = 0
        result = ''
        while right > left:
            clone = s[left:right + 1]
            if s[left:right + 1] == clone[::-1]:
                if len(clone) > longest_palindromic:
                    longest_palindromic = len(clone)
                    result = clone
                    left = right
                    right += 1
                else:
                    right += 1
        return result
