from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = []
        result = []
        for i in range(1, m + 1):
            P.append(i)
        for i in range(len(queries)):
            a = P.index(queries[i])
            value = P[a]
            result.append(a)
            P.remove(value)
            P.insert(0,value)

        return result

