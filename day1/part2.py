numbers = set(map(int, open('input')))
diffs = {2020 - num for num in numbers}
for diff in diffs:
    for num in numbers:
        if diff - num in numbers:
            print(num * (diff - num) * (2020 - diff))
            break
    else:
        continue
    break
