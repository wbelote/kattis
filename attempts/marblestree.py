"""
Each child with a net surplus will need n moves toward that child
Each child with a net deficit will need n moves from that child

moves = sum for each child:
    abs(vertices - marbles) + downstream moves
"""

"""
This works great on the sample input, but gives a wrong answer on the second.

I think there must be some unusual case that I've forgotten to account for. I thought it might be trees with one node,
already solved trees, or deeper trees, but all of those seem to work.
"""
import sys


class Node:
    def __init__(self, data, vin=1):
        me = data[vin]
        self.info = me[0]
        self.marbles_at = me[1]
        self.n_children = me[2]
        self.id_children = me[3:]
        self.children = []
        for c in self.id_children:
            self.children.append(Node(data, vin=c))

    @property
    def vertices(self):
        return 1 + sum([c.vertices for c in self.children])

    @property
    def marbles(self):
        return self.marbles_at + sum([c.marbles for c in self.children])

    def count_moves(self):
        total = 0
        for c in self.children:
            total += abs(c.vertices - c.marbles)
            total += c.count_moves()
        return total


def main():
    n = int(sys.stdin.readline())
    while n:
        vertices = [[]] + [[int(x) for x in sys.stdin.readline().split()] for i in range(n)]
        children = set()
        for i in range(n):
            child = vertices[i+1][3:]
            for c in child:
                children.add(c)
        total = set(range(1, n + 1))
        top = total - children
        tree = Node(vertices, vin=top.pop())
        print(tree.count_moves())

        n = int(sys.stdin.readline())


main()
