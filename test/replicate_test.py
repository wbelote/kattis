import sys


def mutate(layout):
    rows = len(layout)
    cols = len(layout[0])

    neighbors = [[0 for x in range(cols + 2)] for y in range(rows + 2)]

    for r in range(rows):
        for c in range(cols):
            if layout[r][c] == ".":
                continue
            for dr in range(3):
                for dc in range(3):
                    neighbors[r+dr][c+dc] += 1

    return [[[".", "#"][neighbors[y][x] % 2] for x in range(cols + 2)] for y in range(cols + 2)]


def main():
    rows, cols = [int(x) for x in sys.stdin.readline().split()]
    layout = [sys.stdin.readline().rstrip() for r in range(rows)]

    print()
    new = mutate(layout)
    for row in new:
        print("".join(row))


if __name__ == '__main__':
    main()
