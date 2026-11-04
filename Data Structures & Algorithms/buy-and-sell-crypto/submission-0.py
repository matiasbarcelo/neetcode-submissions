class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_amount = 0
        for i in range(len(prices) - 1):
            curr = prices[i]
            rest = prices[i+1:]
            calc = max(rest) - curr
            if calc > max_amount:
                max_amount = calc
        
        return max_amount