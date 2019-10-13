import sys


def dist(a, b):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return (dx ** 2 + dy ** 2) ** 0.5


def time(a, b):
    d = dist(a, b)
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
    cannons = []
    for i in range(n):
        line = sys.stdin.readline().split()
        cannons.append([float(x) for x in line])
    cannons.append(b)

    # Dijkstra
    dists = [time(a, c) for c in cannons] + [time(a, b)]
    unseen = list(range(n + 1))
    while True:
        new = dists.index(min(dists))
        if new == n:
            print(dists[n])
            return
        unseen.remove(new)
        for loc in unseen:
            t = time(cannons[new], cannons[loc])
            if dists[new] + t < dists[loc]:
                dists[loc] = t


if __name__ == '__main__':
    main()
