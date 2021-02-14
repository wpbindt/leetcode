from typing import Set


def shortest(string: str, targets: Set[str]) -> str:
    counter = {
        target: 0
        for target in targets
    }
    to_hit = targets
    left = 0
    right = 1
    if string[left] in counter:
        counter[string[left]] += 1
        to_hit -= {string[left]}
    if string[right] in counter:
        counter[string[right]] += 1
        to_hit -= {string[right]}

    while to_hit:
        right += 1
        if string[right] in targets:
            counter[string[right]] += 1
            to_hit -= {string[right]}

    shortest_sub = string

    while True:
        while True:
            if string[left] in counter:
                if counter[string[left]] <= 1:
                    break
                counter[string[left]] -= 1
            left += 1

        if len(string[left:right+1]) < len(shortest_sub):
            shortest_sub = string[left:right+1]

        while right < len(string) - 1:
            right += 1
            if string[right] in counter:
                counter[string[right]] += 1
            if string[right] == string[left]:
                break
        else:
            return shortest_sub


assert shortest('xyzabcd', {'x', 'y', 'z'}) == 'xyz'
assert shortest('xayzabxyzcd', {'x', 'y', 'z'}) == 'xyz'

