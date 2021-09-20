import itertools
from dataclasses import dataclass


class SpaceIt:
    def __init__(self, space):
        self._space = space
        self._it = iter(self._space.points)

    def __next__(self):
        return self._space[next(self._it)]


class Space:
    def __init__(self):
        self.points = set()

    def __contains__(self, item):
        if isinstance(item, Point):
            item = item.coords

        return item in self.points

    def __getitem__(self, item):
        if isinstance(item, Point):
            item = item.coords

        active = item in self
        return Point(*item, active=active)

    def __iter__(self):
        return SpaceIt(self)

    def add(self, item):
        if item.active:
            self.points.add(item.coords)

    def draw(self):
        minx = min(point.x for point in self)
        maxx = max(point.x for point in self)
        miny = min(point.y for point in self)
        maxy = max(point.y for point in self)
        minz = min(point.z for point in self)
        maxz = max(point.z for point in self)

        for layer in range(minz, maxz + 1):
            print(f'\n\nz={layer}')
            for row in range(miny, maxy + 1):
                for col in range(minx, maxx + 1):
                    if (col, row, layer) in self:
                        print('#', end='')
                    else:
                        print('.', end='')
                print('')

    def simulate(self, fourdim=False):
        newspace = set()

        points = set(self)
        for point in self:
            for other in point.adjacent(fourdim=fourdim):
                points.add(other)

        for point in points:
            count = sum(self[other].active for other in point.adjacent(fourdim=fourdim))
            keep = point.active and count in (2, 3)
            activate = not point.active and count == 3
            if keep or activate:
                newspace.add(point.coords)

        self.points = newspace

    def count_active(self):
        return len(self.points)


@dataclass
class Point:
    x: int
    y: int
    z: int
    w: int = 0
    active: bool = False

    def __add__(self, other):
        if not isinstance(other, tuple):
            raise TypeError('Expected type tuple')

        return Point(*(coord + add for coord, add in zip(self.coords, other)))

    def __hash__(self):
        return hash(self.coords)

    @property
    def coords(self):
        return self.x, self.y, self.z, self.w

    def adjacent(self, fourdim=False):
        if not fourdim:
            moves = itertools.product((-1, 0, 1), repeat=3)
        else:
            moves = itertools.product((-1, 0, 1), repeat=4)

        for move in moves:
            if all(coord == 0 for coord in move):
                continue
            yield self + move


def read_input():
    space = Space()
    with open('input') as f:
        for y, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            for x, char in enumerate(line):
                active = (char == '#')
                space.add(Point(x=x, y=y, z=0, w=0, active=active))

    return space


def part1():
    space = read_input()
    # space.draw()
    for _ in range(6):
        space.simulate(fourdim=False)
    # space.draw()

    return space.count_active()


def part2():
    space = read_input()
    for _ in range(6):
        space.simulate(fourdim=True)

    return space.count_active()



if __name__ == '__main__':
    print('Part 1:', part1())
    print('Part 2:', part2())
