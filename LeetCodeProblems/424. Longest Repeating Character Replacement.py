class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        ans = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


s = Solution()
print(s.characterReplacement(s="AABABBA", k=1))
