from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        num_operations = 0
        for operation in logs:
            if operation != './' and operation != '../':
                num_operations += 1
            elif operation == '../':
                if num_operations != 0:
                    num_operations -= 1

        if num_operations <= 0:
            return 0
        else:
            return num_operations


s = Solution()
print(s.minOperations())
