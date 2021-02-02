from typing import List

# For n pairs: there are n different possibs:
# first paren is paired with character in pos 1
# first paren is paired with character 3
# ...
# first paren is paired with character 2n - 1
# 
# this leads to obv recursive solution, which has 
# O(3^n) running time. Can be solved with dynamic
# programming


def generate_parens(n: int) -> List[str]:
    ...


assert generate_parens(0) == [0]
assert generate_parens(1) == ['()']
assert set(generate_parens(2)) == {'()()', '(())'}
assert set(generate_parens(3)) == {
    '((()))', '(())()', '()(())', '()()()', '(()())'
}

