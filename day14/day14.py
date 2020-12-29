import itertools


def read_input():
    with open('input') as f:
        for line in f:
            instr, val = line.strip().split(' = ')
            if instr.startswith('mem'):
                pos = int(instr.split('[')[1].split(']')[0])
                val = (pos, int(val))
                instr = 'mem'
            yield instr, val


def part1():
    memory = {}
    mask = {}
    for instr, arg in read_input():
        if instr == 'mask':
            mask = arg
        else:
            mempos, num = arg
            num = bin(num)[2:].zfill(36)
            num = [a if a != 'X' else b for a, b in zip(mask, num)]
            memory[mempos] = int(''.join(num), 2)

    return sum(memory.values())


def floating(address):
    floats = [idx for idx, val in enumerate(address) if val == 'X']
    for comb in itertools.product(('0', '1'), repeat=len(floats)):
        for pos, val in zip(floats, comb):
            address[pos] = val
        yield ''.join(address)


def part2():
    memory = {}
    mask = {}
    for instr, arg in read_input():
        if instr == 'mask':
            mask = arg
        else:
            mempos, num = arg
            mempos = bin(mempos)[2:].zfill(36)
            address = [a if a != '0' else b for a, b in zip(mask, mempos)]
            for mempos in floating(address):
                memory[int(mempos, 2)] = num

    return sum(memory.values())


if __name__ == '__main__':
    print('Part 1:', part1())
    print('Part 2:', part2())
