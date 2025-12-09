with open("input.txt") as f:
    lines = f.readlines()

total = 0
for line in lines:
    line = line.strip()
    digits = [(c) for c in line]
    permutations = []

    for i in range(1, len(digits)):
        for j in range(i, len(digits)):
            permutations.append(int(digits[i - 1] + digits[j]))
    total += max(permutations)

print("Part 1:", total)  # 17408

total = 0
required_length = 12
for line in lines:
    line = line.strip()
    digits = [c for c in line]
    result = []
    i = 0

    while len(result) < required_length and i < len(digits):
        needed = required_length - len(result)
        available = len(digits) - i
        look_ahead = available - needed + 1
        largest_digit = max(digits[i : i + look_ahead])

        for j in range(i, i + look_ahead):
            if digits[j] == largest_digit:
                result.append(digits[j])
                i = j + 1
                break

    total += int("".join(result))

print("Part 2:", total)  # 172740584266849
