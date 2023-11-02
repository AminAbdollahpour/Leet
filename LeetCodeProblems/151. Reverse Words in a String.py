class Solution:
    def reverseWords(self, s: str) -> str:
        new = s + ' '
        words_list = []
        skiper = 0
        for i in range(len(new)):

            if len(words_list)==0 or i > skiper:
                if new[i]!=' ':
                    for j in range(i ,len(new)):
                        if new[j]==' ' :
                            words_list.append(new[i:j])
                            skiper = j
                            break
        return ' '.join(reversed(words_list))

