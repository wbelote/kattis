import sys


def compress(x):
    out = []
    for i in range(4):
        if out and x[i] == out[-1]:
            out[-1] += x[i]
        elif x[i]:
            out.append(x[i])

    return out + [0] * (4 - len(out))


def main():
    grid = [[int(x) for x in sys.stdin.readline().split()] for i in range(4)]
    direction = int(sys.stdin.readline())
    if direction % 2:
        d = -direction + 2
        for c in range(4):
            col = [grid[r][c] for r in range(4)]
            col = compress(col[::d])[::d]
            for r in range(4):
                grid[r][c] = col[r]
    else:
        d = -direction + 1
        for i in range(4):
            grid[i] = compress(grid[i][::d])[::d]

    for i in range(4):
        print(grid[i][0], grid[i][1], grid[i][2], grid[i][3], )


main()
