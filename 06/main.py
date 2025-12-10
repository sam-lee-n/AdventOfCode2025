from functools import reduce


with open("input.txt") as f:
    lines = f.readlines()

total = 0
values = []
vstring = []
ops = []
for line in lines:
    line = line.strip()

    if line.count("*") > 0:
        ops.append([x for x in line.split()])
    else:
        values.append([int(x) for x in line.split()])
        vstring.append(line)

for col in range(len(values[0])):
    vertical_values = [values[x][col] for x in range(len(values))]
    if ops[0][col] == "*":
        total += reduce(lambda x, y: x * y, vertical_values, 1)
    elif ops[0][col] == "+":
        total += sum(vertical_values)
print("Part 1:", total)  # 7644505810277


grid = [list(line) for line in lines]
total = 0
val_list = []
for col in range(len(grid[0])):
    vertical_values = [grid[x][col] for x in range(len(grid) - 1)]
    if col < len(grid[-1]) and grid[-1][col] != " ":
        ops = grid[-1][col]

    val = "".join(vertical_values).strip()
    if val.isdigit():
        val_list.append(int(val))
    else:
        if ops == "*":
            total += reduce(lambda x, y: x * y, val_list, 1)
        elif ops == "+":
            total += sum(val_list)
        val_list = []

print("Part 2:", total)  # 12841228084455
