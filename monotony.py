import sys
import math


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


def count(grid, r, c):
    if is_mono(grid, r, c):
        return (2 ** r - 1) * (2 ** c - 1)



def main():
    line = sys.stdin.readline().split()
    r, c = [int(x) for x in line]


main()
