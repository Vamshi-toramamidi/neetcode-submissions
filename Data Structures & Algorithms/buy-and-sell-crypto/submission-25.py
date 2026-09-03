class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        high = prices[0]
        profit = 0
        for i, val1 in enumerate(prices):
            print("val1 :", val1)
            j = i+1
            for val2 in prices[j:]:
                print("val2: ",val2)
                if val2-val1> profit:
                    low = val1
                    high = val2
                    profit = val2-val1
        print("low :",low,"High :", high)
        return profit