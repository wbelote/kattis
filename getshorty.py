import bisect
import sys


# 3 3
# 0 1 0.9
# 1 2 0.9
# 0 2 0.8
# 2 1
# 1 0 1
# 0 0


class Node:
    def __init__(self, x, factor):
        self.id = x
        self.factor = factor

    def __lt__(self, other):
        return self.factor < other.factor

    def __str__(self):
        return str(self.id)


def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    while n and m:
        edges = [[] for _ in range(n)]
        for i in range(m):
            x, y, f = sys.stdin.readline().split()
            x = int(x)
            y = int(y)
            f = float(f)
            edges[x].append(Node(y, f))
            edges[y].append(Node(x, f))

        frontier = [Node(0, 1)]
        visited = set()
        while True:
            new = frontier.pop()
            if new.id == n - 1:
                print("%.4f" % new.factor)
                break
            visited.add(new.id)
            for node in edges[new.id]:
                node.factor *= new.factor
                bisect.insort(frontier, node)
        n, m = [int(x) for x in sys.stdin.readline().split()]


if __name__ == '__main__':
    main()
