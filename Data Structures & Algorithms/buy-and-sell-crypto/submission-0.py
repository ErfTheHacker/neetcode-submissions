class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        minPrice = prices[0]

        for s in prices:
            maxPrice = max(maxPrice, s-minPrice)
            minPrice = min(minPrice, s)
        return maxPrice
