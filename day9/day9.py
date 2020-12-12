from collections import deque


def read_input():
    with open('input') as f:
        for line in f:
            yield int(line)


def part1():
    buffer = deque(maxlen=25)
    for number in read_input():
        # initial buffer fill
        if len(buffer) < buffer.maxlen:
            buffer.append(number)
            continue

        # check all numbers in the buffer
        for other in buffer:
            # pair must be different
            if number == other * 2:
                continue
            # found a pair of numbers that sum up to ours
            if number - other in buffer:
                break
        else:
            # no pair found. this is our solution.
            return number

        # append to the buffer and remove the oldest element
        buffer.append(number)


def part2(search: int):
    current = deque()
    for number in read_input():
        current.append(number)
        total = sum(current)

        while total > search:
            current.popleft()
            total = sum(current)

        if total == search:
            break

    return min(current) + max(current)


if __name__ == '__main__':
    one = part1()
    print('Part 1:', one)
    print('Part 2:', part2(one))
