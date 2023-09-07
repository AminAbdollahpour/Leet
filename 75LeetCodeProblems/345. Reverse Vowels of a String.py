class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        l , r = 0 , len(s) - 1
        while l < r:
            if s_list[l] in vowels and s_list[r] in vowels:
                s_list[l] , s_list[r] = s_list[r] , s_list[l]
                l += 1
                r -= 1
            else:
                if s_list[l] not in vowels:
                    l += 1
                if s_list[r] not in vowels:
                    r -= 1
        return ''.join(s_list)