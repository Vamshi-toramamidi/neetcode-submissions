from typing import List
import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b),
        }

        for tk in tokens:
            if tk in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[tk](a, b))
            else:
                stack.append(int(tk))

        return stack.pop()