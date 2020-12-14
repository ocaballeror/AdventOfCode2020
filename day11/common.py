import itertools
from enum import Enum


class Seat(str, Enum):
    EMPTY = "L"
    TAKEN = "#"
    FLOOR = "."


class Grid:
    def __init__(self, data, height, width):
        self.data = data
        self.height = height
        self.width = width

    def _idx(self, idx) -> slice:
        if isinstance(idx, tuple):
            x, y = idx
            if x < 0 or y < 0:
                raise IndexError('Negative index not allowed')
            if x >= self.height:
                raise IndexError(f'Exceeded height: {idx}')
            if y >= self.width:
                raise IndexError(f'Exceeded width: {idx}')
            return x * self.width + y
        else:
            if idx >= self.height:
                raise IndexError('Row does not exist')
            return slice(self.width * idx, self.width * (idx + 1))

    def __getitem__(self, idx):
        return self.data[self._idx(idx)]

    def __setitem__(self, idx, item):
        self.data[self._idx(idx)] = item

    def __contains__(self, item):
        try:
            self[item]
            return True
        except IndexError:
            return False

    def __len__(self):
        return self.height

    def __iter__(self):
        for idx, elem in enumerate(self.data):
            yield idx // self.width, idx % self.width, elem

    def copy(self):
        return Grid(self.data.copy(), self.height, self.width)


def read_input():
    with open('input') as f:
        lines = f.readlines()
        data = [Seat(c) for line in lines for c in line.strip()]
    return Grid(data, len(lines), len(data) // len(lines))


def directions(x, y):
    for movex, movey in [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]:
        def _vector():
            for i in itertools.count(1):
                yield x + movex * i, y + movey * i
        yield _vector()


