import sys


class Queue:
    def __init__(self):
        self.data = []
        self.start = 0
        self.end = 0

    def enq(self, val):
        self.data.append(val)
        self.end += 1

    def deq(self):
        if self.is_empty:
            return None
        out = self.data[self.start]
        self.start += 1
        return out

    @property
    def is_empty(self):
        return self.start == self.end


class Map:
    def __init__(self, data, dim):
        self.data = data
        self.rows = dim[0]
        self.cols = dim[1]

        self.visited = {}
        self.visited_all = set()
        self.zone_map = {}
        self.max_zone = 0

    def match(self, query):
        start = query[0] * self.cols + query[1]
        end = query[2] * self.cols + query[3]
        if self.data[start] != self.data[end]:
            return 0
        seen = [start in self.visited_all, end in self.visited_all]
        if seen[0] and seen[1]:
            return (self.zone_map[start] == self.zone_map[end]) * (int(self.data[start]) + 1)
        elif seen[1] or seen[0]:
            return 0
        else:
            return self.search(start, end)

    def search(self, start, end):
        out = 0
        zone = self.max_zone
        self.max_zone += 1
        queue = self.visited[zone] = Queue()
        queue.enq(start)
        while not queue.is_empty:
            node = queue.deq()
            if node == end:
                out = int(self.data[start]) + 1
            self.visited_all.add(node)
            self.zone_map[node] = zone
            adj = node - self.cols
            if node // self.cols > 0 and adj not in queue.data and self.data[adj] == self.data[node]:
                queue.enq(adj)
            adj = node + self.cols
            if node // self.cols < self.rows - 1 and adj not in queue.data and self.data[adj] == self.data[node]:
                queue.enq(adj)
            adj = node - 1
            if node % self.cols > 0 and adj not in queue.data and self.data[adj] == self.data[node]:
                queue.enq(adj)
            adj = node + 1
            if node % self.cols < self.cols - 1 and adj not in queue.data and self.data[adj] == self.data[node]:
                queue.enq(adj)
        return out


def main():
    rows, cols = [int(x) for x in sys.stdin.readline().split()]
    kind_map = ""
    for r in range(rows):
        kind_map += sys.stdin.readline().rstrip()
    area = Map(kind_map, [rows, cols])

    n = int(sys.stdin.readline())
    queries = [[int(x) - 1 for x in sys.stdin.readline().split()] for _ in range(n)]

    for q in queries:
        match = area.match(q)
        print(["neither", "binary", "decimal"][match])


if __name__ == '__main__':
    main()
