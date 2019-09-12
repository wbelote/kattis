import sys, math


def main():
    s = int(sys.stdin.readline())
    print(f"{s}:")
    for i in range(2, math.ceil(s / 2) + 1):
        if s % (i + i - 1) in (0, i):
            print(f"{i},{i - 1}")

        if s % i == 0:
            print(f"{i},{i}")


main()
