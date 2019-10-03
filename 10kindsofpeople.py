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


def main():
    rows, cols = [int(x) for x in sys.stdin.readline().split()]
    layout = [sys.stdin.readline().rstrip() for i in range(rows)]

    n = int(sys.stdin.readline())
    queries = [[int(x) - 1 for x in sys.stdin.readline().split()] for i in range(n)]

    zone_map = [[cols * r + c for c in range(cols)] for r in range(rows)]
    zone_list = [{(i // cols, i % cols)} for i in range(rows*cols)]

    for r in range(rows):
        for c in range(cols):
            char = layout[r][c]
            zone = zone_map[r][c]
            adjacent = neighbors(r, c, rows, cols)
            adj_match = []
            zones = [zone]
            for loc in adjacent:
                if layout[loc[0]][loc[1]] == char:
                    adj_match.append(loc)
                    zones.append(zone_map[loc[0]][loc[1]])
            new = min(zones)
            for z in zones:
                print(z)
                members = zone_list[z]
                for m in members:
                    print(m)
                    zone_map[m[0]][m[1]] = new
                zone_list[new] |= zone_list[z]
                zone_list[z] -= zone_list[new]

    active = {}
    for i, z in enumerate(zone_list):
        if z:
            active[i] = len(active)

    for r in range(rows):
        print(" ".join([str(active[x]) for x in zone_map[r]]))

    for q in queries:
        if zone_map[q[0]][q[1]] == zone_map[q[2]][q[3]]:
            print(["binary", "decimal"][int(layout[q[0]][q[1]])])
        else:
            print("neither")


if __name__ == '__main__':
    main()
