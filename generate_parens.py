from typing import List


def generate_parens(n: int) -> List[str]:
    ...


assert generate_parens(0) == [0]
assert generate_parens(1) == ['()']
assert set(generate_parens(2)) == {'()()', '(())'}
assert set(generate_parens(3)) == {
    '((()))', '(())()', '()(())', '()()()', '(()())'
}

