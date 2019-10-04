import sys


class Queue:
    def __init__(self, size=1024):
        self.data = [None] * size
        self.start = 0
        self.end = 0
        self.size = size

    def enq(self, val):
        if (self.start - self.end) % self.size == 1:
            new = [self.deq() for _ in range(self.size)] + [None] * self.size
            self.data = new
            self.start = 0
            self.end = 0
            self.size *= 2

        self.data[self.end] = val
        self.end += 1
        self.end %= self.size

    def deq(self):
        if self.is_empty:
            return None
        out = self.data[self.start]
        self.start += 1
        self.start %= self.size
        return out

    @property
    def is_empty(self):
        return self.start == self.end


def neighbors(pos, r, c, layout):
    out = []
    if pos // c > 0 and layout[pos - c] == layout[pos]:
        out += [pos - c, ]
    if pos // c < r - 1 and layout[pos + c] == layout[pos]:
        out += [pos + c, ]
    if pos % c > 0 and layout[pos - 1] == layout[pos]:
        out += [pos - 1, ]
    if pos % c < c - 1 and layout[pos + 1] == layout[pos]:
        out += [pos + 1, ]
    return out


def search(graph, start, finish, size):
    visited = set()
    queue = Queue(size)
    queue.enq(start)
    while not queue.is_empty:
        node = queue.deq()
        if node == finish:
            return True
        adj = graph[node]
        for n in adj:
            if n not in visited:
                queue.enq(n)
        visited.add(node)
    return False


def main():
    rows, cols = [int(x) for x in sys.stdin.readline().split()]
    kind_map = ""
    for r in range(rows):
        kind_map += sys.stdin.readline().rstrip()

    n = int(sys.stdin.readline())
    queries = [[int(x) - 1 for x in sys.stdin.readline().split()] for _ in range(n)]

    graph = [neighbors(i, rows, cols, kind_map) for i in range(rows * cols)]

    for q in queries:
        start = q[0] * cols + q[1]
        end = q[2] * cols + q[3]
        if search(graph, start, end, rows * cols):
            print(["binary", "decimal"][int(kind_map[start])])
        else:
            print("neither")


if __name__ == '__main__':
    main()
