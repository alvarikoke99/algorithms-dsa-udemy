from collections import deque

"""
Dado un String que solamente contiene los caracteres '(', ')', '{', '}', '[' y ']',
implementa un algoritmo para determinar si es válido.

Ejemplo 1:
 Input: "([]){}"
 Output: True

Ejemplo 2:
 Input: "({)}"
 Output: False
"""


class ValidParenthesis:
    def is_valid(self, s: str) -> bool:
        stack: deque = deque()

        for char in s:
            if not stack or stack[-1] != self.get_opposite(char):
                stack.append(char)
            else:
                stack.pop()
        print(stack)
        return len(stack) == 0
    
    def get_opposite(seld, s: str):
        if s == ")": return "("
        if s == "}": return "{"
        if s == "]": return "["
        return ""