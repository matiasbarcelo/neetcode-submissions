class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_amount = 0
        l = prices[0]

        for i in range(len(prices) - 1):
            # we want to start on the right pointer
            i = i + 1

            r = prices[i]
            calc = r - l

            if calc < 0:
                l = r
            elif calc > max_amount:
                max_amount = calc

        return max_amount