import bisect
import sys


def main():
    n = int(sys.stdin.readline())
    edges = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
    frontier = [[-edges[0][1], [0, 1], 2]]
    while True:
        new = frontier.pop()
        add = new[2]
        if add == n:
            print(-new[0])
            break
        left = [new[0] - edges[new[1][0]][add], [add] + new[1], add + 1]
        right = [new[0] - edges[new[1][-1]][add], new[1] + [add], add + 1]
        bisect.insort(frontier, left)
        bisect.insort(frontier, right)


if __name__ == '__main__':
    main()
