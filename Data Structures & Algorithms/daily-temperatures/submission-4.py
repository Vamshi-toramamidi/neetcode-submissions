class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return 0

        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                st, si = stack.pop()
                res[si] = i - si
            stack.append((temp,i))
        return res