import sys


def neighbors(pos, r, c, layout):
    out = (pos,)
    if pos // c > 0 and layout[pos - c] == layout[pos]:
        out += (pos - c,)
    if pos // c < r - 1 and layout[pos + c] == layout[pos]:
        out += (pos + c,)
    if pos % c > 0 and layout[pos - 1] == layout[pos]:
        out += (pos - 1,)
    if pos % c < c - 1 and layout[pos - 1] == layout[pos]:
        out += (pos + 1,)
    return out


def main():
    rows, cols = [int(x) for x in sys.stdin.readline().split()]
    kind_map = ""
    for r in range(rows):
        kind_map += sys.stdin.readline().rstrip()

    n = int(sys.stdin.readline())
    queries = [[int(x) - 1 for x in sys.stdin.readline().split()] for _ in range(n)]

    zone = [0] * rows * cols
    max_zone = 0
    actual = [0]

    for pos in range(rows * cols):
        paths = neighbors(pos, rows, cols, kind_map)
        path_zones = {actual[zone[p]] for p in paths if zone[p]}
        if not path_zones:
            max_zone += 1
            actual.append(max_zone)
            for p in paths:
                zone[p] = max_zone
        else:
            new = min(path_zones)
            while new != actual[new]:
                new = actual[new]
            for p in paths:
                if zone[p] != 0:
                    actual[zone[p]] = new
                zone[p] = new

    update = [actual[x] for x in actual]
    while actual != update:
        actual = update
        update = [actual[x] for x in actual]
    actual = update

    # print()
    # for r in range(rows):
    #     for c in range(cols):
    #         print(chr(actual[zone[r * cols + c]] + 32), end=" ")
    #         # print(actual[zone[r * cols + c]], end=" ")
    #     print()
    # print()
    # print(actual)
    # print()

    for q in queries:
        start = q[0] * cols + q[1]
        end = q[2] * cols + q[3]
        if actual[zone[start]] == actual[zone[end]]:
            print(["binary", "decimal"][int(kind_map[start])])
        else:
            print("neither")


if __name__ == '__main__':
    main()
