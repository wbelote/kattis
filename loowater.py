import sys


def calc_price(heads, knights):
    if len(knights) < len(heads):
        return -1
    total = 0
    for head in heads:
        while knights[0] < head:
            knights.pop(0)
            if len(knights) < len(heads):
                return -1
        total += knights.pop(0)
    return total


def main():
    while True:
        line = sys.stdin.readline().split()
        n, m = [int(x) for x in line]
        if n + m == 0:
            return

        heads = [int(sys.stdin.readline()) for i in range(n)]
        knights = [int(sys.stdin.readline()) for i in range(m)]
        heads.sort()
        knights.sort()

        total = calc_price(heads, knights)
        if total == -1:
            print("Loowater is doomed!")
        else:
            print(total)


main()
