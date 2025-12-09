from textwrap import wrap

with open("input.txt") as f:
    lines = f.readlines()
values_pairs = lines[0].split(",")

total = 0
for pair in values_pairs:
    start, stop = map(int, pair.split("-"))

    for i in range(start, stop + 1):
        width = len(str(i))
        if width % 2 != 0:
            continue
        if str(i)[0 : width // 2] == str(i)[width // 2 :]:
            total += i

print("Part 1:", total)  # 18700015741

total = 0
for pair in values_pairs:
    start, stop = map(int, pair.split("-"))

    for i in range(start, stop + 1):
        word = str(i)
        width = len(word)
        for j in range(1, width // 2 + 1):
            chunks = wrap(word, width=j)
            if chunks.count(chunks[0]) == len(chunks):
                total += i
                break

print("Part 2:", total)  # 20077272987
