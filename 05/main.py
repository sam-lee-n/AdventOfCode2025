import itertools

with open("input.txt") as f:
    lines = f.readlines()


def merge_ranges(ranges):
    if not ranges:
        return []

    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged = [sorted_ranges[0]]

    for current in sorted_ranges[1:]:
        last = merged[-1]
        if current[0] <= last[1] + 1:
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            merged.append(current)

    return merged


def count_values_in_ranges(ranges):
    return sum(r[1] - r[0] + 1 for r in ranges)


ranges = []
values = []
for line in lines:
    line = line.strip()
    if line == "":
        continue

    if line.count("-") > 0:
        ranges.append([int(x) for x in line.split("-")])
    else:
        values.append(int(line))

fresh = 0
for value in values:
    for r in ranges:
        if r[0] <= value <= r[1]:
            fresh += 1
            break

print("Part 1:", fresh)  # 681

merged_ranges = merge_ranges(ranges)
unique_count = count_values_in_ranges(merged_ranges)
print("Part 2:", unique_count)
