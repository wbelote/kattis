import sys
import math


def main():
    d, v = [int(x) for x in sys.stdin.readline().split()]
    while d + v:
        print(((d ** 3) - ((6 * v) / math.pi)) ** (1 / 3))
        d, v = [int(x) for x in sys.stdin.readline().split()]


main()
