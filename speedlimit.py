import sys


def main():
    while True:
        n = int(sys.stdin.readline())
        if n == -1:
            return
        last = 0
        total = 0
        for i in range(n):
            line = sys.stdin.readline().split()
            s, t = [int(x) for x in line]
            total += s * (t - last)
            last = t
        print(total, "miles")


main()
