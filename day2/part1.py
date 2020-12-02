import re


with open('input') as f:
    count = 0
    for line in f:
        match = re.search(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line)
        lo, hi, search, text = match.groups()
        lo, hi = int(lo), int(hi)
        if lo <= text.count(search) <= hi:
            count += 1

print(count)
