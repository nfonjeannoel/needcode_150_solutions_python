from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        l = 0
        for r in range(len(prices)):
            best = max(best, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
        return best


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n):
                best = max(best, prices[j] - prices[i])
        return best

class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
    print(sol.maxProfit([7, 6, 4, 3, 1]))  # Output: 0
    print(sol.maxProfit([1, 2, 3, 4, 5]))  # Output: 4
    print(sol.maxProfit([5, 4, 3, 2, 1]))  # Output: 0
    print(sol.maxProfit([]))  # Output: 0
