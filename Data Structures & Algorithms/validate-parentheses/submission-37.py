class Solution:
    def isValid(self, s: str) -> bool:
        dicti = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }
        stack = []
        for par in s:
            if par in dicti:
                if stack and stack[-1] == dicti[par]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)
                
        return False if stack else True
