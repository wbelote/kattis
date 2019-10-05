import random

rows = cols = 1000
queries = 1000

text = f"{rows} {cols}\n"
grid = []
for r in range(rows):
    grid.append("")
    for c in range(cols):
        if r and c:
            prob = 0.1
            prob += 0.4 * int(grid[r][c - 1])
            prob += 0.4 * int(grid[r - 1][c])
        elif r:
            prob = 0.1 + 0.8 * int(grid[r - 1][c])
        elif c:
            prob = 0.1 + 0.8 * int(grid[r][c - 1])
        else:
            prob = 0.5
        grid[r] += str(int(random.random() < prob))

text += "\n".join(grid)
text += f"\n{queries}\n"
for i in range(queries):
    line = [str(random.randint(1, rows)) for _ in range(4)]
    text += " ".join(line) + "\n"

with open("map.txt", "w") as f:
    f.write(text)
