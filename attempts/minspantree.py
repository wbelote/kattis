import sys


class Connections:
    def __init__(self, size):
        self.data = list(range(size))

    def get(self, x):
        while x != self.data[x]:
            x = self.data[x]
        return x

    def join(self, a, b):
        new = min(self.get(a), self.get(b))
        while self.data[a] != new:
            new_a = self.data[a]
            self.data[a] = new
            a = new_a
        while self.data[b] != new:
            new_b = self.data[b]
            self.data[b] = new
            b = new_b


def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    while n or m:
        if not m:
            print("Impossible")
            n, m = [int(x) for x in sys.stdin.readline().split()]
            continue
        edges = []
        for i in range(m):
            u, v, w = [int(x) for x in sys.stdin.readline().split()]
            edges.append([w, min(u, v), max(u, v)])
        edges.sort()

        tree = []
        cost = 0
        con = Connections(n)
        for i in range(n - 1):
            new = edges.pop(0)
            while con.get(new[1]) == con.get(new[2]) and edges:
                new = edges.pop(0)
            if con.get(new[1]) == con.get(new[2]):
                break
            con.join(new[1], new[2])
            tree.append(new[1:])
            cost += new[0]
            if not edges:
                break

        if len(tree) < n - 1:
            print("Impossible")
        else:
            print(cost)
            tree.sort()
            for e in tree:
                print(e[0], e[1])

        n, m = [int(x) for x in sys.stdin.readline().split()]


if __name__ == '__main__':
    main()
