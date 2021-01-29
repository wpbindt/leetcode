def roman_to_int(s: str) -> int:
    ...


roman_dict = {
    '': 0,
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}
for roman_digit, arabic_numeral in roman_dict.items():
    for n in range(1, 4):
        assert roman_to_int(n * roman_digit) == n * arabic_numeral

assert roman_to_int('MCMLXX') == 1970
assert roman_to_int('DI') == 501
assert roman_to_int('CD') == 400
assert roman_to_int('XLII') == 42

