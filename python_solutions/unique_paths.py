def unique_paths(n: int, m: int) -> int:
    """
    How many paths are there from top left
    to bottom right on an m x n grid, moving
    only down and right? binom(n + m - 2, m - 1)
    --> recurrence relation and obvious dynamic
    prog solution w O(n*m) time, O(min(n, m)) space
    """
    if n < m:
        return unique_paths(m, n)

    prev_column = m * [1]
    for _ in range(n - 1):
        column = [1]
        while len(column) < m:
            column.append(column[-1] + prev_column[len(column)])
        prev_column = column

    return prev_column[-1]

