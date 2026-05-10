class Solution:
    def maximumProfit(
        self, profit: List[int], weight: List[int], capacity: int
    ) -> int:
        dp = [0] * (capacity + 1)

        for uprofit, uweight in zip(profit, weight):
            for rem_cap in range(uweight, capacity + 1):
                dp[rem_cap] = max(dp[rem_cap], uprofit + dp[rem_cap - uweight])

        return dp[capacity]