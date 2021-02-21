from typing import List

# two windows, one coming from left, one from right
# move in the same way as in the one buy/sell solution, ---- this is not specific enough
# what if we only move the one that currently has the lowest max profit?
# should each iteration move the window only a bit, or complete the whole cycle?


def max_profit(price: List[int]) -> int:
    """
    May buy and sell at most twice
    """
    buy_left = 0
    sell_left = 0
    left_max = 0

    buy_right = len(price) - 1
    sell_right = len(price) - 1
    right_max = 0

    while buy_right >= sell_left:
        right_max = max(
            right_max, 
            price[sell_right] - price[buy_right]
        )
        left_max = max(
            left_max, 
            price[sell_left] - price[buy_left]
        )
        if left_max <= right_max:
            if price[sell_left] < price[buy_left]:
                buy_left = sell_left
            sell_left += 1
        else:
            if price[sell_right] < price[buy_right]:
                sell_right = buy_right
            buy_right -= 1

    return left_max + right_max


assert max_profit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
assert max_profit([5, 4, 3, 2, 1]) == 0
assert max_profit([1, 2, 3, 4, 5]) == 4
assert max_profit([1]) == 0
assert max_profit([1, 2]) == 1
assert max_profit([1, 2, 3]) == 2
assert max_profit([6,1,3,2,4,7]) == 7

