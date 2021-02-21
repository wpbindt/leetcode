from typing import List


def max_profit(prices: List[int]) -> int:
    """
    May buy and sell at most twice
    Let p[i, k] be the max profit on k sales given price[:i+1]
    Then:
        - p[0, k] = 0 for all k
        - p[i, 0] = 0 for all i
        - p[i, k] = max(
            p[i - 1, k],  # buy and sell k times in [:i]
            p[j, k - 1] - price[j] + price[i]  # buy and sell k-1 times in [:j+1], then buy at j, sell at i
            for j = 0..i
          )

    Naive caching implementation is O(n^2), which is too slow.
    By keeping track of the maximum of profit[k - 1][ix] - prices[ix], can reduce to linear, probably
    """
    # profit[k][ix] := max profit with k+1 sales in [:ix+1]
    profit = []
    profit.append(len(prices) * [0])
    profit.append([])
    profit.append([])

    for k in range(1, 3):
        profit[k].append(0)
        for sell_price in prices[1:]:
            profit[k].append(max(
                profit[k][-1],
                *(
                    profit[k - 1][ix] - buy_price + sell_price
                    for ix, buy_price in enumerate(prices[:len(profit[k])])
                )
            ))

    return profit[2][-1]


assert max_profit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
assert max_profit([5, 4, 3, 2, 1]) == 0
assert max_profit([1, 2, 3, 4, 5]) == 4
assert max_profit([1]) == 0
assert max_profit([1, 2]) == 1
assert max_profit([1, 2, 3]) == 2
assert max_profit([6,1,3,2,4,7]) == 7

