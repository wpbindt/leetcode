from collections import deque


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False

    digits_deque = deque()
    while x:
        digits_deque.appendleft(x % 10)
        x //= 10
    
    while digits_deque:
        leftmost_digit = digits_deque.popleft()
        try:
            rightmost_digit = digits_deque.pop()
        except IndexError:
            break
        if leftmost_digit != rightmost_digit:
            return False

    return True


def lame_solution(x: int) -> bool:
    return str(x) == str(x)[::-1]


for solution in [is_palindrome, lame_solution]:
    assert solution(121)
    assert not solution(-121)
    assert solution(1)
    assert not solution(12)

