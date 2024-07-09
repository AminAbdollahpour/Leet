from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        next_idle_time = 0
        total_wait = 0

        for customer in customers:
            next_idle_time = max(customer[0], next_idle_time) + customer[1]
            total_wait += next_idle_time - customer[0]

        return total_wait / len(customers)


s = Solution()
print(s.averageWaitingTime(customers=[[1, 2], [2, 5], [4, 3]]))
