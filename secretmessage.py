import sys, math

n = int(sys.stdin.readline())
for i in range(n):
    line = sys.stdin.readline().strip()
    rows = math.ceil(len(line) ** 0.5)
    line += "*" * (len(line) - rows ** 2)
    out = ""
    for r in range(rows):
        row = ""
        for i in range(r, len(line), rows):
            row = line[i] + row
        out += row

    out = out.replace("*", "")
    print(out)
