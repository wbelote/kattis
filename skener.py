import sys, itertools


def main():
    r, c, zr, zc = [int(x) for x in sys.stdin.readline().split()]
    article = [sys.stdin.readline().rstrip() for i in range(r)]
    for i in range(r):
        line = [c * zc for c in article[i]]
        for j in range(zr):
            print("".join(line))


main()
