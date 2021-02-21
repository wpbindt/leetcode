from math import copysign

def reverse_cheat(x: int) -> int:
    sign = int(copysign(1, x))
    reversed_x = sign * int(str(abs(x))[::-1])
    if reversed_x >= 2**31 or reversed_x < -2**31:
        return 0

    return reversed_x


def reverse(x: int) -> int:
    sign = int(copysign(1, x))
    x *= sign

    digit_stack = []
    while True:
        digit_stack.append(x % 10)
        x //= 10
        if x <= 0:
            break

    exponent = 1
    max_int = (2**31 - (sign == 1))/10
    output = digit_stack.pop()
    while digit_stack:
        digit = digit_stack.pop() * 10**(exponent - 1)

        if digit > max_int - output/10:
            return 0
        
        output += digit * 10
        exponent += 1

    return sign * output

solutions = [reverse_cheat, reverse]

for solution in solutions: 
    assert solution(12) == 21
    assert solution(-1232) == -2321
    assert solution(-2 ** 31) == 0 

