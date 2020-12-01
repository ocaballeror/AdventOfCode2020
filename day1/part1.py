numbers = set(map(int, open('input')))
for num in numbers:
    if 2020 - num in numbers:
        print(num * (2020 - num))
        break
