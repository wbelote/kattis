import sys


def main():
    r, c = [int(x) for x in sys.stdin.readline().split()]
    while r or c:
        cols = ["" for i in range(c)]
        for i in range(r):
            line = sys.stdin.readline()
            for j in range(c):
                cols[j] += line[j]

        cols_s = sorted(cols, key=str.casefold)
        for i in range(r):
            for j in range(c):
                print(cols_s[j][i], end="")
            print()

        r, c = [int(x) for x in sys.stdin.readline().split()]


if __name__ == '__main__':
    main()
