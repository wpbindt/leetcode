from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Initial way of finding this: keep left
    and right pointer, right pointer iterating
    through prices, and moving left pointer to
    right as soon as right is absolutely smaller
    than left. 
    Apparently very similar to max sub array prob
    which has Kadane's algorithm

    Time: O(n)
    Space: O(1)
    """
    min_price = float('inf')
    profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = max(profit, price - min_price)

    return profit
