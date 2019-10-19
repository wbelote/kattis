# Will Belote
# Black Friday (2.2)
# https://open.kattis.com/problems/blackfriday

import sys


def main():
    n = int(sys.stdin.readline())
    line = sys.stdin.readline().split()
    a = [int(x) for x in line]

    for i in range(6, 0, -1):
        if a.count(i) == 1:
            print(a.index(i))
            return

    print("none")


main()
