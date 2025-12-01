with open("input.txt") as f:
    lines = f.readlines()

pos = 50
hit_zero = 0

for i in range(len(lines)):
    line = lines[i].strip()
    direction = line[0]
    steps = int(line[1:])

    if direction == "R":
        pos += steps
    elif direction == "L":
        pos -= steps
    pos %= 100

    if pos == 0:
        hit_zero += 1

print("Part 1:", hit_zero)  # 1064

## part 2
pos = 50
hit_zero = 0
for i in range(len(lines)):
    line = lines[i].strip()
    direction = line[0]
    steps = int(line[1:])

    if direction == "R":
        pos += steps
        hit_zero += pos // 100
        if (pos % 100) == 0:
            hit_zero -= 1
    elif direction == "L":
        hit_zero -= 1 if pos == 0 else 0
        pos -= steps
        hit_zero += abs(pos // 100)
        if (pos % 100) == 0 & abs(pos // 100) > 0:
            hit_zero -= 1

    pos %= 100

    if pos == 0:
        hit_zero += 1

print("Part 2:", hit_zero)  # 6122
