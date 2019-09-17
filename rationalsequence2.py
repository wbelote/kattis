import sys


def parent(x):
    a, b = x
    if a < b:
        return [a, b - a]
    else:
        return [a - b, b]


def main():
    p = int(sys.stdin.readline())
    for i in range(p):
        line = sys.stdin.readline().split()
        k = line[0]
        a, b = [int(x) for x in line[1].split("/")]
        path = []
        now = [a, b]
        while now != [1, 1]:
            path = [now[0] > now[1]] + path
            now = parent(now)

        total = 1
        for right in path:
            total *= 2
            total += right

        print(k, total)


main()
