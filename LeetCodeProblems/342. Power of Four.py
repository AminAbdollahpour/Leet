class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(16):
            power = 4**i
            if power == n:
                return True
            if power > n:
                return False
        return False