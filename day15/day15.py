def read_input():
    with open('input') as f:
        return list(map(int, f.read().strip().split(',')))


def simulate(target):
    start = read_input()
    last = start[-1]
    log = {val: idx + 1 for idx, val in enumerate(start[:-1])}

    for turn in range(len(start), target):
        if last not in log:
            current = 0
        else:
            current = turn - log[last]

        log[last] = turn
        last = current

    return last


if __name__ == '__main__':
    print('Part 1:', simulate(2020))
    print('Part 2:', simulate(int(3e7)))
