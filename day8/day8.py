def read_input():
    with open('input') as f:
        code = [(line.split()[0], int(line.split()[1])) for line in f]
    return code


def run(code):
    acc = 0
    seen = set()
    pc = 0
    while pc not in seen and pc < len(code):
        seen.add(pc)
        inst, arg = code[pc]
        if inst == 'acc':
            acc += arg
        elif inst == 'nop':
            pass
        elif inst == 'jmp':
            pc += arg - 1
        pc += 1

    return pc < len(code), acc


def part1():
    return run(read_input())[1]


def part2():
    code = read_input()
    nopjumps = [i for i, inst in enumerate(code) if inst[0] in ('nop', 'jmp')]
    for idx in nopjumps:
        inst, arg = code[idx]
        if inst == 'nop':
            code[idx] = ('jmp', arg)
        else:
            code[idx] = ('nop', arg)

        loops, acc = run(code)
        if not loops:
            return acc

        code[idx] = (inst, arg)


if __name__ == '__main__':
    print('Part 1:', part1())
    print('Part 2:', part2())
