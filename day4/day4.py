import re

def read_input():
    with open('input') as f:
        content = f.read()

    return [dict(field.split(':') for field in passport.split()) for passport in content.split('\n\n')]

def validate_hgt(val):
    match = re.search(r'(\d+)(cm|in)', val)
    if not match:
        return False

    number, units = match.groups()
    if units == 'cm':
        return 150 <= int(number) <= 193
    elif units == 'in':
        return 59 <= int(number) <= 76
    raise ValueError('huh?')

fields = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': validate_hgt,
    'hcl': lambda x: re.search('^#[0-9a-f]{6}$', x, flags=re.I),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: re.search(r'^\d{9}$', x),
    'cid': lambda x: True,
}

passports = read_input()
expected = set(fields.keys()) - {'cid'}
part1 = sum(expected <= psp.keys() for psp in passports)
print('Part 1:', part1)

valid = 0
for psp in passports:
    for key, validate in fields.items():
        if key == 'cid':
            continue
        if not (key in psp and validate(psp[key])):
            break
    else:
        valid += 1

print('Part 2:', valid)
