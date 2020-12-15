def read_input():
    with open('input') as f:
        return [(line[0], int(line[1:])) for line in f]


def turn(current, move_dir, move_deg):
    sides = ['E', 'S', 'W', 'N']
    assert move_deg % 90 == 0
    rotation = move_deg // 90
    if move_dir == 'L':
        rotation = -rotation
    new = (sides.index(current) + rotation) % len(sides)
    return sides[new]


def transpose(vector, move_dir, move_deg):
    vecx, vecy = vector
    turns = move_deg % 360 // 90
    if move_dir == 'L':
        turns = 4 - turns
    for _ in range(turns):
        vecx, vecy = -vecy, vecx

    return vecx, vecy


def move(direction, tiles, pos):
    posx, posy = pos
    if direction == 'E':
        return (posx + tiles, posy)
    if direction == 'W':
        return (posx - tiles, posy)
    if direction == 'N':
        return (posx, posy - tiles)
    if direction == 'S':
        return (posx, posy + tiles)


def part1():
    pos = (0, 0)
    direction = 'E'
    for instruction, arg in read_input():
        if instruction in ('L', 'R'):
            direction = turn(direction, instruction, arg)
        elif instruction == 'F':
            pos = move(direction, arg, pos)
        else:
            pos = move(instruction, arg, pos)

    return abs(pos[0]) + abs(pos[1])


def part2():
    pos = (0, 0)
    waypoint = (10, -1)
    for instruction, arg in read_input():
        if instruction in ('L', 'R'):
            waypoint = transpose(waypoint, instruction, arg)
        elif instruction == 'F':
            pos = pos[0] + waypoint[0] * arg, pos[1] + waypoint[1] * arg
        else:
            waypoint = move(instruction, arg, waypoint)

    return abs(pos[0]) + abs(pos[1])


if __name__ == '__main__':
    print('Part 1:', part1())
    print('Part 2:', part2())
