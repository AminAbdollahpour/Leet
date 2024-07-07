class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        emptyBottle = 0
        drank = 0
        while numBottles != 0:
            emptyBottle += numBottles
            drank += numBottles
            numBottles = emptyBottle // numExchange
            emptyBottle -= numExchange * numBottles

        return drank

