class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def vow(n):
            return n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u'

        current_max = 0
        for i in range(k):
            if vow(s[i]):
                current_max += 1
        maximum = current_max
        for i in range(k, len(s), 1):
            if vow(s[i - k]): current_max -= 1
            if vow(s[i]): current_max += 1
            maximum = max(current_max, maximum)
        return maximum


