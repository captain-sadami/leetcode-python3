class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp_diff = 0
        for i, l in enumerate(prices):
            if i == len(prices):
                break
            for j, r in enumerate(prices[i+1:]):
                diff = r - l
                if diff > temp_diff:
                    temp_diff = diff
        if temp_diff > 0:
            return temp_diff
        return 0
