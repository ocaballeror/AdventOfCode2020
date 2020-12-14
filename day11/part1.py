from common import Seat, read_input, directions


def move(grid):
    prev = grid.copy()
    mods = 0
    for x, y, seat in prev:
        adjacent = len([
            move for vector in directions(x, y)
            if (move := next(vector)) in prev and prev[move] == Seat.TAKEN
        ])

        if seat == Seat.EMPTY and adjacent == 0:
            grid[x, y] = Seat.TAKEN
            mods += 1
        elif seat == Seat.TAKEN and adjacent >= 4:
            grid[x, y] = Seat.EMPTY
            mods += 1

    return mods


def simulate():
    grid = read_input()
    while move(grid) > 0:
        pass

    return len([seat for row in grid for seat in row if seat == Seat.TAKEN])


if __name__ == '__main__':
    print('Part 1:', simulate())
