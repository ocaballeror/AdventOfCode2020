from functools import lru_cache


def read_input():
    with open('input') as f:
        return sorted(map(int, f))

def part1():
    adapters = read_input()
    diffs = []
    for idx, adp in enumerate(adapters):
        if idx == 0:
            diff = adp
        else:
            diff = adp - adapters[idx - 1]
        diffs.append(diff)

    # extra diff of 3 for our actual device
    diffs.append(3)

    return diffs.count(1) * diffs.count(3)


@lru_cache
def combinations(idx, adapters):
    """
    Count the possible combinations for an index in the list of adapters.

    For example, for the list 1,2,3,4,5:

    Combinations for the first element (1) should be the sum of the combinations for two, three and four, because 12, 13
    and 14 are all possible sequences. Thus we need to recursively count the possible sequences starting with two, three
    and four and sum them all up to get our result. Notice the use of `@lru_cache` to memoize intermediate results for
    this function.
    """
    if idx == len(adapters) - 1:
        return 1
    else:
        number = adapters[idx]
        idx += 1
        count = 0
        while idx < len(adapters) and adapters[idx] - number <= 3:
            count += combinations(idx, adapters)
            idx += 1
        return count


def part2():
    adapters = read_input()
    adapters = (0, *adapters, adapters[-1] + 3)
    return combinations(0, adapters)


if __name__ == '__main__':
    print('Part 1:', part1())
    print('Part 2:', part2())
