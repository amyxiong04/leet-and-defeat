class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0

        while right <= len(prices) - 1:
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else: # if any cheaper buy price, immediately go to that price. even if it doesnt end being max profit, the max so far is saved
                # but if max is later, than the profit will be more since this number is smaller (consider [3, 9, 2, 4, 7])
                left = right
            right += 1

        return maxProfit