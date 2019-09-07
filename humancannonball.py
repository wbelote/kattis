import sys, math
from itertools import permutations as itper


def dist(a, b):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return math.sqrt(dx ** 2 + dy ** 2)


def calc_time(path):
    total = dist(path[0], path[1]) / 5
    for i in range(2, len(path)):
        d = dist(path[i - 1], path[i])
        if d <= 30:
            total += d / 5
        else:
            total += 2
            total += abs(d - 50) / 5
    return total


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

    # go through all possible paths
    best_time = dist(a, b)
    for p in itper(range(n + 1), n):
        path = [a]
        for x in p:
            if x == n:
                path.append(b)
                break
            else:
                path.append(cannons[x])

        time = calc_time(path)
        if time < best_time:
            best_time = time
            print(path, time)

    print(best_time)


main()
