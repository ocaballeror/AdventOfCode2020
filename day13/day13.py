import itertools


def read_input():
    with open('input') as f:
        timestamp = int(next(f))
        buses = [int(bus) if bus != 'x' else bus for bus in next(f).split(',')]

    return timestamp, buses


def part1():
    timestamp, buses = read_input()
    diffs = [(bus - (timestamp % bus), bus) for bus in buses if bus != 'x']
    wait, bus = min(diffs)
    return wait * bus


def part2():
    _, buses = read_input()
    ref = buses[0]
    start = 0
    step = 1
    for idx, bus in enumerate(buses[1:]):
        if bus == 'x':
            continue
        for i in itertools.count(start, step):
            if (ref * i) % bus == (bus - idx - 1) % bus:
                break

        start = i
        step *= bus

    return start * ref



if __name__ == '__main__':
    print('Part 1:', part1())
    print('Part 2:', part2())
