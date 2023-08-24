from copy import copy
from typing import List


class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        output = []
        for number in nums:
            newList = copy(nums)
            newList.remove(number)
            product = 1
            for x in newList:
                product = product * x
            output.append(product)
        return output


