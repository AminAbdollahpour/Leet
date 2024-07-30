class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        letter_set = set()
        left = 0
        for i in range(len(s)):
            while s[i] in letter_set:
                letter_set.remove(s[left])
                left += 1
            letter_set.add(s[i])
            ans = max(ans, i - left + 1)
        return ans

