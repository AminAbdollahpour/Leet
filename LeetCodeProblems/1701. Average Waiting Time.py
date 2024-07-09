from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        right_now = customers[0][0]
        total_wait = 0
        for customer in customers:
            if customer[0] < right_now:
                additional_wait = abs(customer[0] - right_now)
                total_wait += customer[1] + additional_wait
            else:
                total_wait += customer[1]
            right_now += customer[1]

        return total_wait / len(customers)


s = Solution()
print(s.averageWaitingTime(customers=[[1, 2], [2, 5], [4, 3]]))
