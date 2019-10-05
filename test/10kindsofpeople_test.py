import time

start_time = time.time()
splits = [[], []]


class Node:
    def __init__(self, q, rows, cols):
        self.rows = rows
        self.cols = cols
        self.r = q[0]
        self.c = q[1]
        self.id = self.r * cols + self.c
        self.dist = abs(self.r - q[2]) + abs(self.c - q[3])

    def adj(self, dr, dc, end):
        return Node([self.r + dr, self.c + dc] + end, self.rows, self.cols)

    def val(self, data):
        return data[self.r][self.c]

    def __lt__(self, other):
        return self.dist > other.dist

    def __str__(self):
        return f"({self.r}, {self.c})"


def search(data, q, rows, cols):
    end = q[2:]
    if data[q[0]][q[1]] != data[q[2]][q[3]]:
        return -1
    frontier = [Node(q, rows, cols)]
    visited = {frontier[0].id}
    while frontier:
        pos = frontier.pop()
        if pos.r == q[2] and pos.c == q[3]:
            return int(pos.val(data))

        if pos.r:
            adj = pos.adj(-1, 0, end)
            if adj.id not in visited and adj.val(data) == pos.val(data):
                frontier.append(adj)
            visited.add(adj.id)
        if pos.c:
            adj = pos.adj(0, -1, end)
            if adj.id not in visited and adj.val(data) == pos.val(data):
                frontier.append(adj)
            visited.add(adj.id)
        if pos.r < rows - 1:
            adj = pos.adj(1, 0, end)
            if adj.id not in visited and adj.val(data) == pos.val(data):
                frontier.append(adj)
            visited.add(adj.id)
        if pos.c < cols - 1:
            adj = pos.adj(0, 1, end)
            if adj.id not in visited and adj.val(data) == pos.val(data):
                frontier.append(adj)
            visited.add(adj.id)
        frontier.sort()
    return -1


def main():
    f = open("map.txt", "r")
    rows, cols = [int(x) for x in f.readline().split()]
    kind_map = []
    for r in range(rows):
        kind_map += [f.readline().rstrip()]

    n = int(f.readline())
    queries = [[int(x) - 1 for x in f.readline().split()] for _ in range(n)]

    i = 0
    for q in queries:
        if i in {0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512}:
            print(i)
        i += 1
        match = search(kind_map, q, rows, cols)
        if match >= 0:
            print(["binary", "decimal", "neither"][match])
    f.close()


if __name__ == '__main__':
    main()
    print(time.time() - start_time)
    print(sum(splits[1]) - sum(splits[0]))
