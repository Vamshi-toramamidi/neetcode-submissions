class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i, val1 in enumerate(prices):
            for val2 in prices[i+1:]:
                if val2-val1> profit:
                    profit = val2-val1
        return profit