import sys


def neighbors(x, y, max_x, max_y):
    out = tuple()
    if x > 0:
        out = out + ((x - 1, y),)
    if x < max_x - 1:
        out = out + ((x + 1, y),)
    if y > 0:
        out = out + ((x, y - 1),)
    if y < max_y - 1:
        out = out + ((x, y + 1),)
    return out


def search(q, layout, r, c):
    start = layout[q[0]][q[1]]
    finish = layout[q[2]][q[3]]
    if start != finish:
        return "neither"

    zone = {q[:2]}
    edge = [q[:2]]
    while True:
        if q[-2:] in edge:
            return ["binary", "decimal"][int(start)]
        edge_new = []
        for pos in edge:
            for n in neighbors(pos[0], pos[1], r, c):
                if layout[n[0]][n[1]] == start and n not in zone:
                    edge_new.append(n)
                    zone.add(n)
        if not edge_new:
            return "neither"
        edge = edge_new


def main():
    rows, cols = [int(x) for x in sys.stdin.readline().split()]
    layout = [sys.stdin.readline().rstrip() for i in range(rows)]

    n = int(sys.stdin.readline())
    queries = [tuple([int(x) - 1 for x in sys.stdin.readline().split()]) for i in range(n)]

    for q in queries:
        is_path = search(q, layout, rows, cols)
        print(is_path)


if __name__ == '__main__':
    main()
