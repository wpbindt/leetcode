from collections import Counter
from typing import List, Set

SUDOKU_SIZE = 9
BOX_WIDTH = 3

def validate_sudoku(board: List[List[int]]) -> bool:
    box_contents = {
        (col_ix, row_ix): set()
        for col_ix in range(0, BOX_WIDTH)
        for row_ix in range(0, BOX_WIDTH)
    }
    column_contents = {
        col_ix: set()
        for col_ix in range(SUDOKU_SIZE)
    }
    for row_ix, row in enumerate(board):
        current_row = set()
        for col_ix, entry in enumerate(row):
            box = (col_ix // BOX_WIDTH, row_ix // BOX_WIDTH)
            if entry != '.':
                if entry in box_contents[box]:
                    return False
                box_contents[box].add(entry)

                if entry in current_row:
                    return False
                current_row.add(entry)

                if entry in column_contents[col_ix]:
                    return False
                column_contents[col_ix].add(entry)

    return True

