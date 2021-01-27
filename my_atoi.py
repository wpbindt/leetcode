def my_atoi(s: str) -> int:
    ...


assert my_atoi('456') == 456
assert my_atoi('    123') == 123
assert my_atoi('  -123') == -123
assert my_atoi('  +123') == 123
assert my_atoi('+123') == 123
assert my_atoi('-123') == -123
assert my_atoi('asdf') == 0
assert my_atoi('   asdf') == 0
assert my_atoi('   1asdf') == 1
assert my_atoi('1 2') == 1

