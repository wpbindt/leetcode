from typing import List


def max_profit(prices: List[int]) -> int:
    """
    The obvious greedy approach (sell as soon as the price drops)
    works, in O(n) time, O(1) space
    """
    profit = 0
    min_price = prices[0]
    for price, next_price in zip(prices, prices[1:]):
        if next_price < price:
            profit += price - min_price
            min_price = next_price

    profit += max(0, prices[-1] - min_price)
    return profit

