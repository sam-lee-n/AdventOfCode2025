with open("input.txt") as f:
    lines = f.readlines()

grid = [list(line.strip()) for line in lines]  # Convert strings to lists of characters
directions = [(-1, -1), (-1, 0), (-1, 1), 
              (0, -1), (0, 1), 
              (1, -1), (1, 0), (1, 1)]

total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != "@":
            continue

        neighbors = []
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[ni]):
                neighbors.append(grid[ni][nj])

        if neighbors.count("@") < 4:
            total += 1

print("Part 1:", total)  # 1346

total = 0
diff = 1

while diff > 0:
    diff = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != "@":
                continue

            neighbors = []
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[ni]):
                    neighbors.append(grid[ni][nj])

            if neighbors.count("@") < 4:
                total += 1
                grid[i][j] = "."
                diff = 1

print("Part 1:", total)  # 8493
