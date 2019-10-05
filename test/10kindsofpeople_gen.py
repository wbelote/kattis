import random

text = "1000 1000\n"
grid = []
for r in range(1000):
    grid.append("")
    for c in range(1000):
        if r and c:
            prob = 0.1
            prob += 0.4 * int(grid[r][c - 1])
            prob += 0.4 * int(grid[r - 1][c])
        elif r:
            prob = 0.01 + 0.98 * int(grid[r - 1][c])
        elif c:
            prob = 0.01 + 0.98 * int(grid[r][c - 1])
        else:
            prob = 0.5
        grid[r] += str(int(random.random() < prob))
text += "\n".join(grid)
text += "\n1000\n"
for i in range(1000):
    line = [str(random.randint(1, 1000)) for _ in range(4)]
    text += " ".join(line) + "\n"
with open("map.txt", "w") as f:
    f.write(text)
