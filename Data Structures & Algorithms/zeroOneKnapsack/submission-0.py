class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        dp = [0] * (M + 1)

        # Base cases
        for c in range(M + 1):
            if weight[0] <= c:
                dp[c] = profit[0]

        for i in range(1, N):
            curr_profit = [0] * (M + 1)
            for c in range(1, M + 1):
                skip = dp[c]
                include = (
                    # Pickup current item + profit of previous pickups
                    profit[i] + dp[c - weight[i]]
                    if c - weight[i] >= 0  # If it still fits
                    else 0
                )
                curr_profit[c] = max(skip, include)
            dp = curr_profit

        return dp[M]