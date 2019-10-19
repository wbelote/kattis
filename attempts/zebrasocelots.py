import sys


def main():
    n = int(sys.stdin.readline())
    total = 0
    for i in range(n - 1, -1, -1):
        if sys.stdin.readline()[0] == "O":
            total += 2 ** i

    print(total)


main()
