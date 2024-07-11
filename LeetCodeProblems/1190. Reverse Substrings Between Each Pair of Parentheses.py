class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ')':
                piece = []
                while stack[-1] != '(':
                    piece.append(stack.pop())
                stack.pop()
                stack.extend(piece)
            else:
                stack.append(i)
        return ''.join(stack)
