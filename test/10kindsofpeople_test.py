import time

start_time = time.time()
splits = [[], [], [],]


class Layout:
    def __init__(self, rows, cols, val_map):
        self.map = val_map
        self.rows = rows
        self.cols = cols

        self.zone = [0] * rows * cols
        self.zone[0] = 1
        self.max_zone = 1
        self.eq = [0, 1]
        self.top = {1}

    def update(self, pos):
        start = time.time()

        adj = pos - self.cols
        if pos // self.cols > 0 and self.map[adj] == self.map[pos]:
            if self.zone[adj] and self.zone[pos]:
                self.merge(self.zone[adj], self.zone[pos])
            elif self.zone[adj]:
                self.zone[pos] = self.zone[adj]
            elif self.zone[pos]:
                self.zone[adj] = self.zone[pos]

        adj = pos + self.cols
        if pos // self.cols < self.rows - 1 and self.map[adj] == self.map[pos]:
            if self.zone[adj] and self.zone[pos]:
                self.merge(self.zone[adj], self.zone[pos])
            elif self.zone[adj]:
                self.zone[pos] = self.zone[adj]
            elif self.zone[pos]:
                self.zone[adj] = self.zone[pos]

        adj = pos - 1
        if pos % self.cols > 0 and self.map[adj] == self.map[pos]:
            if self.zone[adj] and self.zone[pos]:
                self.merge(self.zone[adj], self.zone[pos])
            elif self.zone[adj]:
                self.zone[pos] = self.zone[adj]
            elif self.zone[pos]:
                self.zone[adj] = self.zone[pos]

        adj = pos + 1
        if pos % self.cols < self.cols - 1 and self.map[adj] == self.map[pos]:
            if self.zone[adj] and self.zone[pos]:
                self.merge(self.zone[adj], self.zone[pos])
            elif self.zone[adj]:
                self.zone[pos] = self.zone[adj]
            elif self.zone[pos]:
                self.zone[adj] = self.zone[pos]

        splits[0] += [time.time() - start]

    def merge(self, a, b):
        start = time.time()
        if a < b:
            self.eq[b] = self.get_top(a)
            self.top.remove(b)
        elif b < a:
            self.eq[a] = self.get_top(b)
            self.top.remove(a)
        splits[1] += [time.time() - start]

    def get_top(self, val):
        start = time.time()
        while val not in self.top:
            val = self.eq[val]
        splits[2] += [time.time() - start]
        return val


def main():
    rows, cols = 1000, 1000
    f = open("map.txt", "r")
    kind_map = ""
    for r in range(rows):
        kind_map += f.readline()

    n = 0
    queries = [[int(x) - 1 for x in f.readline().split()] for _ in range(n)]

    layout = Layout(rows, cols, kind_map)
    for i in range(rows * cols):
        layout.update(i)

    names = ["update", "merge", "get top"]
    for i in range(3):
        print(f"{names[i]}: n={len(splits[i])}, total={sum(splits[i])}")

    # print()
    # for r in range(rows):
    #     for c in range(cols):
    #         print(chr(actual[zone[r * cols + c]] + 32), end=" ")
    #         # print(actual[zone[r * cols + c]], end=" ")
    #     print()
    # print()
    # print(actual)
    # print()

    for q in queries:
        start = q[0] * cols + q[1]
        end = q[2] * cols + q[3]
        if layout.get_top(start) == layout.get_top(end):
            print(["binary", "decimal"][int(kind_map[start])])
        else:
            print("neither")

    # diff = [splits[i] - splits[i - 1] for i in range(1, len(splits))]
    # a = sum(diff[0::2])  # 2.29
    # b = sum(diff[1::2])
    # print(a, b)


if __name__ == '__main__':
    main()
    print(time.time() - start_time)

# import random
#
# out = "1000 1000\n"
# for i in range(1000):
#     for j in range(1000):
#         out += random.choice("01")
#     out += "\n"
# out += "0\n"
#
# with open("map.txt", "w") as f:
#     f.write(out)
