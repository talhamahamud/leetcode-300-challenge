class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprofit=float('inf')
        maxprofit=0

        for price in prices:
            if price<minprofit:
                minprofit=price
            else:
                maxprofit=max(maxprofit, price-minprofit)

        return maxprofit