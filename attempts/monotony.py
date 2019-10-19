import sys
import math
from itertools import combinations as itcom


def choose(a, b):
    if b == 1 or a - b == 1:
        return a
    return int(math.factorial(a) / (math.factorial(b) * math.factorial(a - b)))


def is_mono(grid, r, c):
    if r <= 2 and c <= 2:
        return 1

    for row in range(r):
        if grid[row] != sorted(grid[row]) and grid[row][::-1] != sorted(grid[row]):
            return 0

    for col in range(c):
        this = [grid[row][col] for row in range(r)]
        if this != sorted(this) and this[::-1] != sorted(this):
            return 0

    return 1


def main():
    line = sys.stdin.readline().split()
    r, c = [int(x) for x in line]
    grid = []
    for i in range(r):
        line = sys.stdin.readline().split()
        grid.append([int(x) for x in line])

    total = 0
    for h in range(1, r + 1):
        for w in range(1, c + 1):
            if h < 2 and w < 2:
                total += choose(r, h) * choose(c, w)
            else:
                for rows in itcom(range(r), h):
                    for cols in itcom(range(c), w):
                        sub = [[grid[row][col] for col in cols] for row in rows]
                        total += is_mono(sub, h, w)

    print(total)


main()
