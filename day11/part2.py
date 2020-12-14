from common import Seat, read_input, directions


def move(grid):
    prev = grid.copy()
    mods = 0
    for x, y, seat in prev:
        visible = 0
        for vector in directions(x, y):
            while (loc := next(vector)) in prev and prev[loc] == Seat.FLOOR:
                pass

            if loc in prev and prev[loc] == Seat.TAKEN:
                visible += 1

        if seat == Seat.EMPTY and visible == 0:
            grid[x, y] = Seat.TAKEN
            mods += 1
        elif seat == Seat.TAKEN and visible >= 5:
            grid[x, y] = Seat.EMPTY
            mods += 1

    return mods


def simulate():
    grid = read_input()
    while move(grid) > 0:
        pass

    return len([seat for row in grid for seat in row if seat == Seat.TAKEN])


if __name__ == '__main__':
    print('Part 2:', simulate())
