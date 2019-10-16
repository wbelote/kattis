import sys


def calc_time(dists, speeds, c):
    return sum([d / (s + c) for d, s in zip(dists, speeds)])


def main():
    n, t = [int(x) for x in sys.stdin.readline().split()]
    dists = []
    speeds = []
    for _ in range(n):
        di, si = [int(x) for x in sys.stdin.readline().split()]
        dists.append(di)
        speeds.append(si)

    min_c = -min(speeds)
    max_c = min_c + 1
    change_c = 1
    while calc_time(dists, speeds, max_c) > t:
        min_c = max_c
        change_c *= 2
        max_c += change_c

    while True:
        c = (min_c + max_c) / 2
        diff = calc_time(dists, speeds, c) - t
        if abs(max_c - min_c) < 0.000000000001:
            return c
        if abs(diff) < 0.000000001:
            return c
        if diff > 0:
            min_c = c
        if diff < 0:
            max_c = c


if __name__ == '__main__':
    print(main())
