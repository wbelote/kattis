import math
import sys


def main():
    n, k = [int(x) for x in sys.stdin.readline().split()]
    t = []
    for i in range(k):
        t.append(int(sys.stdin.readline()))

    total_processed = 0
    max_total = 0
    for i in range(k, n):
        t.append(int(sys.stdin.readline()))
        if t[i] - t[total_processed] >= 1000:
            total_processed += 1
        else:
            max_total = max([max_total, i - total_processed])

    print(1 + (max_total // k))


main()
