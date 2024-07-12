class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        arr = list(s)
        ans = 0

        def remover(arr, find, y, ans):
            i = 0
            while i < len(arr):
                portion = arr[i:i + 2]
                if ''.join(portion) == find:
                    del arr[i + 1], arr[i]
                    ans += y
                    i = -1
                i += 1
            return ans, arr
        if x >= y:
            first = remover(arr, 'ab', x, ans)
            ans = remover(first[1], 'ba', y, first[0])
        else:
            second = remover(arr, 'ba', y, ans)
            ans = remover(second[1], 'ab', x, second[0])
        return ans[0]


s = Solution()
print(s.maximumGain(s="aabbaaxybbaabb", x=5, y=4))
