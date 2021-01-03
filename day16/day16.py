from collections import defaultdict


def read_input():
    rules = {}
    ticket = []
    others = []
    with open('input') as f:
        section = 'rules'
        for line in map(str.strip, f):
            if not line:
                continue

            if line == 'your ticket:':
                section = 'ticket'
                continue
            elif line == 'nearby tickets:':
                section = 'others'
                continue

            if section == 'rules':
                name, ranges = line.split(':')
                ranges = [
                    range(int(rng.split('-')[0]), int(rng.split('-')[1]) + 1)
                    for rng in ranges.split(' or ')
                ]
                rules[name] = ranges
            elif section == 'ticket':
                ticket = [int(num) for num in line.split(',')]
            elif section == 'others':
                others.append([int(num) for num in line.split(',')])

    return rules, ticket, others


def find_invalids(ticket, rules):
    return [
        num
        for num in ticket
        if not any(num in rng for rule in rules.values() for rng in rule)
    ]


def part1():
    rules, _, others = read_input()
    return sum(
        invalid
        for ticket in others
        for invalid in find_invalids(ticket, rules)
    )


def part2():
    rules, mine, others = read_input()
    # order will map every name to the list of possible indices that match its
    # ruleset
    order = defaultdict(list)
    others = [ticket for ticket in others if not find_invalids(ticket, rules)]
    for idx, group in enumerate(zip(*others)):
        for name, ranges in rules.items():
            if all(any(num in rng for rng in ranges) for num in group):
                order[name].append(idx)

    # solve the `order` dict by keeping the keys that have just one possible
    # value, then remove that value from all the other lists
    mapping = {}
    taken = set()
    while order:
        for key, value in order.items():
            value = [val for val in value if val not in taken]
            order[key] = value
            if len(value) == 1:
                mapping[key] = value[0]
                taken.add(value[0])
                continue

        for key in mapping:
            order.pop(key, None)

    res = 1
    for key, value in mapping.items():
        if key.startswith('departure'):
            res *= mine[value]
    return res


if __name__ == '__main__':
    print('Part 1:', part1())
    print('Part 2:', part2())
