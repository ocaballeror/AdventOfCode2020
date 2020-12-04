def read_input():
    with open('input') as f:
        grid = [[c == '#' for c in line.strip()] for line in f]
    return grid


def traverse(right, down):
    grid = read_input()
    pos = [0, 0]
    trees = 0
    while pos[0] < len(grid):
        if grid[pos[0]][pos[1]]:
            trees += 1
        pos[0] += down
        pos[1] = (pos[1] + right) % len(grid[0])
    return trees


if __name__ == '__main__':
    print('Part 1:', traverse(3, 1))

    part2 = 1
    for moves in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        part2 *= traverse(*moves)
    print('Part 2:', part2)
