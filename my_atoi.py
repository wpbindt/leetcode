from collections import deque


DIGITS = {
    str(a): a
    for a in range(10)
}


def my_atoi(s: str) -> int:
    for ix, c in enumerate(s):
        if c != ' ':
            current_ix = ix
            break
    else:
        return 0

    sign = 1
    if s[current_ix] == '-':
        sign = -1
        current_ix += 1
    elif s[current_ix] == '+':
        current_ix += 1

    digits_queue = deque()
    for c in s[current_ix:]:
        if c not in DIGITS:
            break
        digits_queue.appendleft(DIGITS[c])

    output = 0
    while digits_queue:
        output = 10 * output + digits_queue.pop()

    return sign * output


assert my_atoi('456') == 456
assert my_atoi('0456') == 456
assert my_atoi('    123') == 123
assert my_atoi('  -123') == -123
assert my_atoi('  +123') == 123
assert my_atoi('+123') == 123
assert my_atoi('-123') == -123
assert my_atoi('asdf') == 0
assert my_atoi('   asdf') == 0
assert my_atoi('   1asdf') == 1
assert my_atoi('1 2') == 1
assert my_atoi('    ') == 0
assert my_atoi('    +') == 0

