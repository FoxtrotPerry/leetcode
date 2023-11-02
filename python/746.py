from typing import List


# Approach:
# Calculate the cost it would take to get to each step.
# Because we can take steps two at a time, we'll return the min of the last two step's
# cost sum to get to them.


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] = min(cost[i - 1], cost[i - 2]) + cost[i]
        print(cost)
        return min(cost[-1], cost[-2])
