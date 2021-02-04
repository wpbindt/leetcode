from functools import lru_cache
from itertools import product
import time
from typing import List


@lru_cache(maxsize=None)
def generate_parens(n: int) -> List[str]:
    if n == 0:
        return ['']

    output = []
    for k in range(n):
        for inside, outside in product(
            generate_parens(k), 
            generate_parens(n - 1 - k)
        ):
            output.append('(' + inside + ')' + outside)

    return output


def generate_parens_non_recursive(n: int) -> List[str]:
    possible_parens_list = [[] for _ in range(n+1)]
    possible_parens_list[0].append('')

    for m in range(1, n + 1):
        for k in range(m):
            for inside, outside in product(
                possible_parens_list[k],
                possible_parens_list[m - 1 - k]
            ):
                possible_parens_list[m].append('(' + inside + ')' + outside)

    return possible_parens_list[n]


def generate_parentheses(n: int) -> List[str]:
    if n == 0:
        return ['']
    if n == 1:
        return ['()']

    output = set()
    for shorter_expression in generate_parentheses(n - 1):
        for ix in range(2*(n - 1)):
            output.add(shorter_expression[:ix] + '()' + shorter_expression[ix:])

    return list(output)


for solution in {generate_parens, generate_parens_non_recursive, generate_parentheses}:
    assert solution(0) == ['']
    assert solution(1) == ['()']
    assert set(solution(2)) == {'()()', '(())'}
    assert set(solution(3)) == {
        '()()()', '()(())', '(())()', '(()())', '((()))'
    }

start = time.time()
n = 13
generate_parentheses(n)
end = time.time()
print(f'Takes {end - start} seconds to generate expressions with {n} paren pairs')

