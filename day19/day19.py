index = {}


def read_input():
    with open("input") as f:
        content = f.read().strip().splitlines()

    strings = []
    parsing_rules = True
    for line in content:
        if parsing_rules:
            if not line.strip():
                parsing_rules = False
                continue
            num, rules = line.strip().split(":")
            num = int(num)
            rules = rules.strip()
            if '"' in rules:
                index[num] = rules.strip('"')
            else:
                rules = [list(map(int, path.strip().split())) for path in rules.split(" | ")]
                index[num] = rules

        else:
            strings.append(line)

    return strings


def matches(string, rule):
    for path in index[rule]:
        rem = string
        for otherrule in path:
            if not rem:
                break

            if isinstance(otherrule, str):
                assert len(otherrule) == 1
                match = otherrule == rem[0]
                if match:
                    rem = rem[1:]
            else:
                assert isinstance(otherrule, int)
                match, rem = matches(rem, otherrule)

            if not match:
                break

        if match:
            return True, rem

    return False, rem


def part1():
    strings = read_input()
    count = 0
    for test in strings:
        match, rem = matches(test, 0)
        valid = bool(match and not rem)
        count += valid
    return count


def part2():
    strings = read_input()
    index[8] = [[42], [42, 8]]
    index[11] = [[42, 31], [42, 11, 31]]

    count = 0
    for test in strings:
        match, rem = matches(test, 0)
        valid = bool(match and not rem)
        count += valid
    return count


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
