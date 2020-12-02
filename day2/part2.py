import re


with open('input') as f:
    count = 0
    for line in f:
        match = re.search(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line)
        pos1, pos2, search, text = match.groups()
        char1, char2 = text[int(pos1) - 1], text[int(pos2) - 1]
        if char1 != char2 and (char1 == search or char2 == search):
            count += 1

print(count)
