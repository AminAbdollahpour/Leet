from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        s = []
        for i in range(len(chars)):
            if chars[i] in s:
                continue
            else:
                s.append(chars[i])
                if chars.count(chars[i])>10:
                    s.append(str(chars.count(chars[i]))[0])
                    s.append(str(chars.count(chars[i]))[1])
                elif chars.count(chars[i])>1:
                    s.append(str(chars.count(chars[i])))

        return len(s)

