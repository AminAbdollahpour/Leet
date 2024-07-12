class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        arr = list(s)
        ans = 0
        i = 0
        j = 0
        yba = 'ba'
        xab = 'ab'
        if x > y:
            y, x = x, y
            yba, xab = xab, yba
        while i < len(arr):
            portion = arr[i:i + 2]
            if ''.join(portion) == yba:
                print('wut')
                del arr[i + 1], arr[i]
                ans += y
                i = -1
            i += 1
        print(arr)
        print(ans)
        while j < len(arr):
            portion = arr[j:j + 2]
            if ''.join(portion) == xab:
                print('rot')
                del arr[j + 1], arr[j]
                ans += x
                j = -1
            j += 1
        return ans


s = Solution()
print(s.maximumGain(s="aabbaaxybbaabb", x=5, y=4))
