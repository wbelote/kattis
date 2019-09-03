import sys


def main():
    while True:
        line = sys.stdin.readline().split()
        if len(line) == 1:
            return
        x1, y1, x2, y2, p = [float(x) for x in line]

        print((abs(x1 - x2) ** p + abs(y1 - y2) ** p) ** (1 / p))


main()
