def convert(s: str, num_rows:int) -> str:
    if num_rows == 1:
        return s

    rows = [[] for _ in range(num_rows)]
    for ix, c in enumerate(s):
        ix_mod = ix % (2*num_rows - 2)
        if 0 <= ix_mod < num_rows:
            rows[ix_mod].append(c)
        elif num_rows <= ix_mod:
            rows[2*num_rows-2 - ix_mod].append(c)

    return ''.join(''.join(row) for row in rows)

assert convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
assert convert('PAYPALISHIRING', 1) == 'PAYPALISHIRING'

