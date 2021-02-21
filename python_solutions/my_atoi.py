from collections import deque


DIGITS = {
    str(a): a
    for a in range(10)
}

MAX_VALUE = {
    1: 2 ** 31 - 1,
    -1: 2 ** 31
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
        next_digit = digits_queue.pop()
        if next_digit / 10 > MAX_VALUE[sign] / 10 - output:
            return sign * MAX_VALUE[sign]

        output = 10 * output + next_digit

    return sign * min(MAX_VALUE[sign], output)


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
assert my_atoi('2147483648') == 2147483647

