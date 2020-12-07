import re
from collections import defaultdict, deque


def read_input():
    graph = {}
    with open('input') as f:
        for line in f:
            match = re.search(r'^(([a-z]+ )+)bags contain (.*)\.', line)
            colour = match.group(1).strip()
            contain = match.group(3).strip()
            if contain == 'no other bags':
                contain = []
            else:
                contain = [
                    (int(bag.strip().split()[0]), ' '.join(bag.strip().split()[1:-1]))
                    for bag in contain.split(',')
                ]

            assert colour not in graph, 'Repeated colour?'
            graph[colour] = contain

    return graph


def reverse_dict(graph):
    rev = defaultdict(list)
    for colour, contains in graph.items():
        for _, other in contains:
            rev[other].append(colour)

    return rev


def part1():
    target = 'shiny gold'
    graph = reverse_dict(read_input())
    canhold = set()
    to_visit = deque([target])
    while to_visit:
        first = to_visit.popleft()
        canhold.add(first)
        if first in graph:
            to_visit.extend(colour for colour in graph[first] if colour not in canhold)

    canhold -= {target}
    return len(canhold)


def count_bags(colour, graph, cache):
    if not graph[colour]:
        contains = 0
    else:
        contains = sum(count_bags(other, graph, cache) * count for count, other in graph[colour])
    # +1 because we want to count the bag itself
    cache[colour] = contains + 1
    return contains + 1


def part2():
    # -1 because we don't want to count the shiny gold bag itself
    return count_bags('shiny gold', read_input(), {}) - 1


if __name__ == '__main__':
    print('Part 1:', part1())
    print('Part 2:', part2())
