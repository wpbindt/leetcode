from __future__ import annotations

from typing import Generic, Iterator, List, TypeVar

T = TypeVar('T')


class SliceableMatrix(Generic[T]):
    def __init__(
        self, 
        rows: List[List[T]],
        *, 
        col_slice: slice = slice(None),
        row_slice: slice = slice(None)
    ) -> None:
        self.rows = rows
        self._row_slice = self._remove_nones_from_slice(
            row_slice, 
            replacement_stop=len(rows)
        )
        self._col_slice = self._remove_nones_from_slice(
            col_slice, 
            replacement_stop=len(rows[0])
        )

    @property
    def diag_size(self) -> int:
        col_boundary = min(self._col_slice.stop, len(self.rows[0]))
        row_boundary = min(self._row_slice.stop, len(self.rows))
        return max(
            0,
            min(
                col_boundary - self._col_slice.start,
                row_boundary - self._row_slice.start
            )
        )

    def __iter__(self) -> Iterator[T]:
        yield from [
            element
            for row in self.rows[self._row_slice]
            for element in row[self._col_slice]
        ]

    def __bool__(self) -> bool:
        return self.diag_size > 0

    def __repr__(self) -> str:
        return str([
            row[self._col_slice]
            for row in self.rows[self._row_slice]
        ])

    def __getitem__(self, index) -> Union[T, SliceableMatrix[T]]:
        if not(isinstance(index, tuple) and len(index) == 2):
            raise ValueError('Invalid slice')

        row, col = index[0], index[1]
        if isinstance(row, int) and isinstance(col, int):
            return self._get_single_item(row, col)

        if isinstance(row, int):
            row = slice(row, row + 1, None)
        if isinstance(col, int):
            col = slice(col, col + 1, None)

        return self._get_slice(row, col)

    def _get_single_item(self, row: int, col: int) -> T:
        if self._row_slice.start + row >= self._row_slice.stop:
            raise IndexError('Row index out of range')
        if self._col_slice.start + col >= self._col_slice.stop:
            raise IndexError('Column index out of range')

        return self.rows[
            self._row_slice.start + row
        ][
            self._col_slice.start + col
        ]

    def _get_slice(self, row: slice, col: slice) -> SliceableMatrix[T]:
        row = self._remove_nones_from_slice(row, self._row_slice.stop)
        col = self._remove_nones_from_slice(col, self._col_slice.stop)

        return SliceableMatrix(
            self.rows,
            col_slice=slice(
                self._col_slice.start + col.start, 
                self._col_slice.start + col.stop
            ),
            row_slice=slice(
                self._row_slice.start + row.start, 
                self._row_slice.start + row.stop
            )
        )

    @staticmethod
    def _remove_nones_from_slice(
        slice_: slice, 
        replacement_stop: int
    ) -> slice:
        if slice_.start is None:
            start = 0
        else:
            start = slice_.start
        if slice_.stop is None:
            stop = replacement_stop
        else:
            stop = slice_.stop

        return slice(start, stop)


def search(matrix: SliceableMatrix[int], target: int) -> bool:
    """
    Naive: just search entire matrix -> O(n * m)
    Lower bound: O(log(n * m)), because the matrix
    could be ascending left to right top to bottom
    and searching a sorted list is at best O(log(n))

    Since the search in the beginning iterates over
    the diagonal, this solution is linear, but by
    replacing it with binary search, can get this
    algorithm down to O(log(n)^2)
    """
    if not matrix:
        return False
    diag_sup = 0
    while diag_sup < matrix.diag_size:
        if matrix[diag_sup, diag_sup] > target:
            break
        diag_sup += 1

    if diag_sup == 0:
        return False
    if matrix[diag_sup - 1, diag_sup - 1] == target:
        return True
    
    return (
        search(matrix[:diag_sup, diag_sup:], target)
        or search(matrix[diag_sup:, :diag_sup], target)
    )


if __name__ == '__main__':
    for target in [1, 2, 3, 4]:
        for matrix in [[[1, 2], [3, 4]], [[1, 3], [2, 4]]]:
            assert search(SliceableMatrix(matrix), target)

    for target in [0, 5, 1.5, 2.5, 3.5]:
        for matrix in [[[1, 2], [3, 4]], [[1, 3], [2, 4]]]:
            assert not search(SliceableMatrix(matrix), target)

    assert search(SliceableMatrix([[3]]), 3)
    assert not search(SliceableMatrix([[3]]), 2)
    assert not search(SliceableMatrix([[3, 4]]), 2)
    assert not search(SliceableMatrix([[3, 4, 5]]), 2)
    assert not search(SliceableMatrix([[3, 4, 5, 6]]), 2)
    assert not search(SliceableMatrix([[3], [4]]), 2)
    assert not search(SliceableMatrix([[3], [4], [5]]), 2)

    assert search(SliceableMatrix([[3, 4]]), 3)
    assert search(SliceableMatrix([[3, 4, 5]]), 3)
    assert search(SliceableMatrix([[3, 4, 5, 6]]), 3)
    assert search(SliceableMatrix([[3], [4]]), 3)
    assert search(SliceableMatrix([[3], [4], [5]]), 3)

    matrix = SliceableMatrix(
        [
            [1, 3, 5, 5],
            [1, 4, 20, 21],
            [6, 7, 21, 22],
        ]
    )
    for i in matrix:
        assert search(matrix, i)

    for i in [0, 2, 4.5, 3.5, 20.5, 23]:
        assert not search(matrix, i)

