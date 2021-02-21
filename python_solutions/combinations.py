from typing import List


def is_solution(combi: List[int], k: int) -> bool:
    return len(combi) == k


def next_candidates(
    combi: List[int], 
    n: int
) -> Generator[List[int], None, None]:
    if not combi:
        yield from ([x] for x in range(1, n + 1))
    else:
        yield from (combi + [x] for x in range(combi[-1] + 1, n + 1))


def backtrack(
    n: int, 
    k: int, 
    combi: List[int], 
    combis: List[List[int]]
) -> None:
    if is_solution(combi, k):
        combis.append(combi)
        return

    for candidate in next_candidates(combi, n):
        backtrack(n, k, candidate, combis)

def combinations(n: int, k: int) -> List[List[int]]:
    combis = []
    backtrack(n, k, [], combis)
    return combis
    

