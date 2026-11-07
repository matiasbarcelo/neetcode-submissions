import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+' : lambda a, b: a + b, '-' : lambda a, b: a - b, '*' : lambda a, b: a * b, '/' : lambda a, b: math.trunc(a / b)}
        num_stack = []

        for token in tokens:
            if token not in operators:
                num_stack.append(int(token))
            else:
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                result = operators[token](num1, num2)
                num_stack.append(result)

        if num_stack:
            return num_stack.pop()