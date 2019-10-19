import sys
import math
import bisect


def dist(a, b):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return math.sqrt(dx ** 2 + dy ** 2)


def main():
    cx, cy, n = [int(x) for x in sys.stdin.readline().split()]
    comm = [cx, cy]
    distances = []
    for i in range(n):
        x, y, r = [int(x) for x in sys.stdin.readline().split()]
        d = dist(comm, [x, y]) - r
        distances.append(d)

    distances.sort()

    if distances[1] < distances[2]:
        print(math.ceil(distances[2]) - 1)
    elif distances[0] < distances[1]:
        print(math.ceil(distances[1]) - 1)
    else:
        print(math.ceil(distances[0]) - 1)


main()
