class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pairs(pair, score):
            nonlocal s
            stack = []
            ans = 0
            for letter in s:
                if letter == pair[1] and stack and stack[-1] == pair[0]:
                    stack.pop()
                    ans += score
                else:
                    stack.append(letter)
            s = ''.join(stack)
            return ans

        ans = 0
        pair = 'ab' if x > y else 'ba'
        ans += remove_pairs(pair, max(x, y))
        ans += remove_pairs(pair[::-1], min(x, y))
        return ans


s = Solution()
print(s.maximumGain(s="aabbaaxybbaabb", x=5, y=4))
