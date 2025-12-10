with open("input.txt") as f:
    lines = f.readlines()

grid = [list(line.strip()) for line in lines]
split = 0
for row_index, row in enumerate(grid):
    for col_index, cell in enumerate(row):
        if cell == "S":
            grid[row_index + 1][col_index] = "|"
        elif cell == "^":
            if grid[row_index - 1][col_index] == "|":
                grid[row_index][col_index - 1] = "|"
                grid[row_index][col_index + 1] = "|"
                split += 1
        else:
            if grid[row_index - 1][col_index] == "|":
                grid[row_index][col_index] = "|"
# for row in grid:
#     print("".join(row))
print("Part 1:", split)  # 1662


grid = [list(line.strip()) for line in lines]
for row_index, row in enumerate(grid):
    for col_index, cell in enumerate(row):
        if cell == "S":
            grid[row_index + 1][col_index] = "1"
        elif cell == "^":
            top = (
                0
                if not grid[row_index - 1][col_index].isdigit()
                else int(grid[row_index - 1][col_index])
            )
            left = (
                0
                if not grid[row_index][col_index - 1].isdigit()
                else int(grid[row_index][col_index - 1])
            )
            right = (
                0
                if not grid[row_index][col_index + 1].isdigit()
                else int(grid[row_index][col_index + 1])
            )

            grid[row_index][col_index - 1] = str(sum([top, left]))
            grid[row_index][col_index + 1] = str(sum([top, right]))
        elif (grid[row_index - 1][col_index]).isdigit():
            if cell == ".":
                grid[row_index][col_index] = grid[row_index - 1][col_index]
            else:
                top = int(grid[row_index - 1][col_index])
                grid[row_index][col_index] = str(int(grid[row_index][col_index]) + top)

print("Part 2:", sum([int(x) for x in grid[-1] if x.isdigit()]))  # 40941112789504
