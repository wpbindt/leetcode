from typing import List


def transpose(m: List[List[int]]) -> None:
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            m[i][j], m[j][i] = m[j][i], m[i][j]

def reverse_rows(m: List[List[int]]) -> None:
    for row in m:
        row.reverse()

def rotate(m: List[List[int]]) -> None:
    transpose(m)
    reverse_rows(m)

