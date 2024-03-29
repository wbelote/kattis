# Will Belote
# Eight Queens (3.2)
# https://open.kattis.com/problems/8queens

import sys


def main():
    queens = []
    for i in range(8):
        line = sys.stdin.readline()
        for j in range(8):
            if line[j] == "*":
                queens.append([j, i])

    if len(queens) != 8:
        print("invalid")
        return

    for queen in queens:
        others = queens[:]
        others.remove(queen)
        for other in others:
            if queen[0] == other[0] or queen[1] == other[1]:
                print("invalid")
                return
            if abs(queen[0] - other[0]) == abs(queen[1] - other[1]):
                print("invalid")
                return

    print("valid")


main()
