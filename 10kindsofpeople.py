import sys


def neighbors(x, y, max_x, max_y):
    out = []
    if x > 0:
        out.append([x - 1, y])
    if x < max_x:
        out.append([x + 1, y])
    if y > 0:
        out.append([x, y - 1])
    if y < max_y:
        out.append([x, y + 1])
    return out


def main():
    rows, cols = [int(x) for x in sys.stdin.readline().split()]
    layout = [sys.stdin.readline().rstrip() for i in range(rows)]

    n = int(sys.stdin.readline())
    queries = [[int(x) for x in sys.stdin.readline().split()] for i in range(n)]

    zone_map = [[cols * r + c for c in range(cols)] for r in range(rows)]
    zone_list = []

    for r in range(rows):
        for c in range(cols):
            char = layout[r][c]
            adjacent = neighbors(r, c, rows, cols)
            for loc in adjacent:
                # merge adjacent zone with current zone
                pass


if __name__ == '__main__':
    main()
