from typing import List

TELEPHONE = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def digits_to_letters(digits: str) -> List[str]:
    if not digits:
        return ['']

    return [
        letter + combination
        for letter in TELEPHONE[digits[0]]
        for combination in digits_to_letters(digits[1:])
    ]


assert digits_to_letters('') == ['']
assert set(digits_to_letters('3')) == {'d', 'e', 'f',}
assert set(digits_to_letters('23')) == {
    'ad', 'ae', 'af', 'be', 'bf', 'bd', 'cd', 'ce', 'cf',
}

