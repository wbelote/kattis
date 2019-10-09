import bisect
import sys


def main():
    n = int(sys.stdin.readline())
    items = [int(x) for x in sys.stdin.readline().split()]
    m = int(sys.stdin.readline())
    edges = [[None for a in range(n)] for b in range(n)]
    neighbors = [[] for _ in range(n)]
    for i in range(m):
        a, b, dist = [int(x) for x in sys.stdin.readline().split()]
        edges[a - 1][b - 1] = edges[b - 1][a - 1] = dist
        neighbors[a - 1] += [b - 1]
        neighbors[b - 1] += [a - 1]

    frontier = [[0, items[0], [0]]]
    seen = set()
    while frontier:
        new = frontier.pop()
        new_id = new[2][-1]
        if new_id == n - 1:  # and (frontier[0][0] > new[0] or frontier[0][1] > new[1]):
            print(-new[0], new[1])
            return
        seen.add(new_id)
        for e in neighbors[new_id]:
            if e not in seen:
                dist = edges[new_id][e]
                bisect.insort(frontier, [new[0] - dist, new[1] + items[e], new[2] + [e]])
    print("impossible")


if __name__ == '__main__':
    main()
