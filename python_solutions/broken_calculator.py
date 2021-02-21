from math import log


def moves(x: int, y: int) -> int:
    operations = 0
    while y > x:
        if y % 2:
            y += 1
        else:
            y //= 2
        operations += 1

    return operations + x - y


assert moves(1, 1) == 0
assert moves(5, 8) == 2  # subtract one, multiply by 2
assert moves(5, 10) == 1
assert moves(5, 4) == 1
assert moves(5, 3) == 2
assert moves(4, 11) == 4  # subtract one, multiply by 4, subtract one
assert moves(3, 10) == 3

