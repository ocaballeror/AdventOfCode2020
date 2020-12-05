def read_input():
    with open('input') as f:
        return [line.strip() for line in f]


def bsearch(pattern, lo, hi):
    for char in pattern:
        if char in ('B', 'R'):
            lo = (lo + hi) // 2 + 1
        elif char in ('F', 'L'):
            hi = (lo + hi) // 2
        else:
            raise ValueError(f'What is {char}')

    assert lo == hi, 'Binary search not completed?'
    return lo


def part1():
    highest = 0
    for bpass in read_input():
        row = bsearch(bpass[:7], 0, 127)
        col = bsearch(bpass[7:], 0, 7)
        seatid = row * 8 + col
        highest = max(highest, seatid)
    return highest


def part2():
    # assume all seats are missing and remove them from the set as we find them
    # in our input. We exclude the first and last row from the beginning
    # because the puzzle description says our seat is not there
    missing = {(row, col) for col in range(8) for row in range(1, 127)}
    for bpass in read_input():
        row = bsearch(bpass[:7], 0, 127)
        col = bsearch(bpass[7:], 0, 7)
        missing.remove((row, col))

    # look for the one id that doesn't have its +1 or its -1 in the list
    missing_ids = {row * 8 + col for row, col in missing}
    for seatid in sorted(missing_ids):
        if seatid - 1 not in missing_ids and seatid + 1 not in missing_ids:
            return seatid

    raise ValueError('Seat ID not found')


if __name__ == '__main__':
    print('Part 1:', part1())
    print('Part 2:', part2())
