import sys
import math


def ssd(b, n):
    total = 0
    digits = int(math.log(n, b)) + 1
    for i in range(digits):
        d = (n // b ** i) % b
        total += d ** 2
    return total


def main():
    p = int(sys.stdin.readline())
    for i in range(p):
        k, b, n = [int(x) for x in sys.stdin.readline().split()]
        b = int(b)
        print(k, ssd(b, n))


main()
