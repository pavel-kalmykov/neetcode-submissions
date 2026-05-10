class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        def max_profit_from_element_having_capacity(
            i: int, remaining_capacity: int
        ) -> int:
            if i == len(weight):
                return 0
            if memo[i][remaining_capacity] != -1:
                return memo[i][remaining_capacity]

            skip = max_profit_from_element_having_capacity(i + 1, remaining_capacity)

            take = skip
            if (new_capacity := remaining_capacity - weight[i]) >= 0:
                take = profit[i] + max_profit_from_element_having_capacity(
                    i, new_capacity
                )

            memo[i][remaining_capacity] = max(skip, take)
            return memo[i][remaining_capacity]

        memo = [[-1] * (capacity + 1) for _ in range(len(weight))]
        return max_profit_from_element_having_capacity(0, capacity)
