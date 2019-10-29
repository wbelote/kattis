import random

edges = []
for i in range(20):
    for j in range(i + 1, 20):
        edges.append([i, j])
random.shuffle(edges)
edges = edges[:30]
edges.sort()

out = "20 30\n"
for i in range(30):
    e = edges.pop(0)
    w = random.randint(0, 100)
    out = f"{out}{e[0]} {e[1]} {w}\n"

with open("minspantree.txt", "w") as f:
    f.write(out)
