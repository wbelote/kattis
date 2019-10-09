import bisect
import sys


def main():
    n = int(sys.stdin.readline())
    edges = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
    frontier = [[edges[0][1], [0, 1]]]
    while True:
        new = frontier.pop(0)
        add = len(new[1])
        if add == n:
            print(new[0] - n + 2)
            break
        frontier += [[edges[new[1][0]][add] + new[0] + 1, [add] + new[1]]] + [[edges[new[1][-1]][add] + new[0] + 1, new[1] + [add]]]
        frontier.sort()


if __name__ == '__main__':
    main()
