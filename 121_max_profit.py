from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        current_min = prices[0]
        max_profit = 0

        for price in prices:
            if price < current_min:
                current_min = price
            else:
                current_profit = price - current_min
                if current_profit > max_profit:
                    max_profit = current_profit

        return max_profit


x = Solution()
print(x.maxProfit([2, 4, 1]))
