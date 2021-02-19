from typing import List


def merge(l1: List[int], l2: List[int]) -> List[int]:
    ix1 = 0
    ix2 = 0
    output = []
    while ix1 < len(l1) and ix2 < len(l2):
        el1 = l1[ix1]
        el2 = l2[ix2]
        if el1 < el2:
            output.append(el1)
            ix1 += 1
        else:
            output.append(el2)
            ix2 += 1

    if ix1 < len(l1):
        output.extend(l1)

    if ix2 < len(l2):
        output.extend(l2)

    return output


def remove_by_index(string: str, removal_stack: List[int]) -> str:
    while removal_stack:
        ix = removal_stack.pop()
        string = string[:ix] + string[ix + 1:]
    return string


def remove_parens(string: str) -> str:
    open_parens_stack = []
    removal_stack = []
    for ix, char in enumerate(string):
        if char == '(':
            open_parens_stack.append(ix)
        elif char == ')':
            if open_parens_stack:
                open_parens_stack.pop()
            else:
                removal_stack.append(ix)

    removal_stack = merge(removal_stack, open_parens_stack)
    return remove_by_index(string, removal_stack)


assert remove_parens('') == ''
assert remove_parens('a') == 'a'
assert remove_parens('()') == '()'
assert remove_parens('(') == ''
assert remove_parens(')') == ''
assert remove_parens(')(') == ''
assert remove_parens('a()') == 'a()'
assert remove_parens('(ab)') == '(ab)'
assert remove_parens('(a)b)') == '(a)b'
assert remove_parens('(a)(b') == '(a)b'
assert remove_parens(')(a)(b') == '(a)b'
assert remove_parens('ab(a)(b') == 'ab(a)b'
assert remove_parens('ab(a(b))(b)') == 'ab(a(b))(b)'
assert remove_parens('(ab(a(b))(b)') == 'ab(a(b))(b)'

