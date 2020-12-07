def read_input():
    with open('input') as f:
        return f.read().strip().split('\n\n')

def part1():
    total = 0
    for group in read_input():
        answers = set(x for x in group.replace('\n', ''))
        total += len(answers)

    return total


def part2():
    total = 0
    for group in read_input():
        answers = [set(answ) for answ in group.split()]
        total += len(set.intersection(*answers))

    return total


if __name__ == '__main__':
    print('Part 1:', part1())
    print('Part 2:', part2())
