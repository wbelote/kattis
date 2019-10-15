import bisect
import sys


def dist(a, b):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return (dx ** 2 + dy ** 2) ** 0.5


def time(a, b, start_id):
    d = dist(a, b)
    if start_id == 0:
        return d / 5
    if d <= 30:
        return d / 5
    return 2 + abs(50 - d) / 5


def main():
    # get start and finish points
    line = sys.stdin.readline().split()
    a = [float(x) for x in line]
    line = sys.stdin.readline().split()
    b = [float(x) for x in line]

    # get list of cannon positions
    n = int(sys.stdin.readline())
    cannons = [a]
    for i in range(n):
        line = sys.stdin.readline().split()
        cannons.append([float(x) for x in line])
    cannons.append(b)

    # Dijkstra
    frontier = [[0, 0]]
    seen = set()
    while True:
        new = frontier.pop(0)
        if new[1] == n + 1:
            print(new[0])
            return
        if new[1] in seen:
            continue
        seen.add(new[1])
        for loc in range(1, n + 2):
            if loc not in seen:
                t = time(cannons[new[1]], cannons[loc], new[1])
                bisect.insort(frontier, [new[0] + t, loc])


if __name__ == '__main__':
    main()
