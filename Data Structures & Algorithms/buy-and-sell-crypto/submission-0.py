class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        p1 = p2 = 0

        while p2 < len(prices):
            ans = max(ans, prices[p2] - prices[p1])

            if prices[p2] < prices[p1]:
                p1 = p2
            
            p2 += 1
        
        return ans