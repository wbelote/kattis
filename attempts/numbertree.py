# Ben, Trevor, Will
import sys


def main():
    line = sys.stdin.readline().split()
    height = int(line[0])
    if len(line) == 1:
        print(2 ** (height + 1) - 1)
        return
    path = line[1]

    level = height - len(path)
    n = 2 ** (height + 1) - 2 ** len(path)

    d = 1
    while path:
        if path[-1] == "R":
            n -= d
        path = path[:-1]
        d *= 2

    print(n)


main()
