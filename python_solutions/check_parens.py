OPEN_PARENS = {
    '(': ')',
    '{': '}',
    '[': ']',
}


def check_parens(s: str) -> bool:
    parens_stack = []
    for c in s:
        if c in OPEN_PARENS:
            parens_stack.append(c)
        else:
            try:
                open_paren = parens_stack.pop()
            except IndexError:
                return False

            if OPEN_PARENS[open_paren] != c:
                return False

    if parens_stack:
        return False
    return True


assert check_parens('()')
assert check_parens('')
assert not check_parens('(')
assert not check_parens(')')
assert check_parens('([{}])')
assert check_parens('()[]{}')
assert not check_parens('({)}')

