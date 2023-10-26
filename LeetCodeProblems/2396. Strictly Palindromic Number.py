class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def numberToBase(num, base):
            if num == 0:
                return [0]
            digits = []
            while num:
                digits.append(int(num % base))
                num //= base
            return digits[::-1]


        for i in range(2,n - 1):
            print(numberToBase(n, i))
            if numberToBase(n, i) != numberToBase(n, i)[::-1]:
                return False
        return True

