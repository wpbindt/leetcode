from typing import List


class SliceableMatrix:
    def __init__(self, lists: List[List], *, start=(0,0), stop=None):
        self.lists = lists
        if stop is None:
            stop = (len(lists), len(lists[0]))
        self.stop = stop
        self.start = start

    def __iter__(self):
        yield from [
            row[self.start[1]:self.stop[1] + 1] 
            for row in self.lists[self.start[0]:self.stop[0] + 1]
        ]

    def __getitem__(self, index):
        if not(isinstance(index, tuple) and len(index) == 2):
            raise ValueError('Invalid slice')
            
        row, col = index[0], index[1]
        if isinstance(row, int) and isinstance(col, int):
            if not (
                self.start[0] + row <= self.stop[0] 
                and self.start[1] + col <= self.stop[1]
            ):
                raise IndexError('Index out of range')
            return self.lists[self.start[0] + row]][self.start[1] + col]
        
        if isinstance(row, int):
            row = slice(row, row+1, None)
        if isinstance(col, int):
            col = slice(col, col+1, None)
        
        return SliceableMatrix(
            self.lists,
            start=(self.start[0] + row.start, self.start[1] + col.start),
            stop=(self.start[0] + row.stop, self.start[1] + col.stop)
        )

# bin search the diagonal
# this partitions the matrix in four
# quadrants
# search #2 and #3
# --> O(nlog(n))-ish solution when n = m


def search(matrix: List[List[int]], target: int) -> bool:
    """
    Naive: just search entire matrix -> O(n * m)
    Lower bound: O(log(n * m)), because the matrix
    could be ascending left to right top to bottom
    and searching a sorted list is at best O(log(n))
    """
    ...

