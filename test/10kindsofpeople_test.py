import time

start_time = time.time()


def neighbors(pos, r, c, layout):
    out = (pos,)
    if pos // c > 0 and layout[pos - c] == layout[pos]:
        out += (pos - c,)
    if pos // c < r - 1 and layout[pos + c] == layout[pos]:
        out += (pos + c,)
    if pos % c > 0 and layout[pos - 1] == layout[pos]:
        out += (pos - 1,)
    if pos % c < c - 1 and layout[pos - 1] == layout[pos]:
        out += (pos + 1,)
    return out


def main():
    rows, cols = 1000, 1000
    f = open("map.txt", "r")
    kind_map = ""
    for r in range(rows):
        kind_map += f.readline()

    n = 0
    queries = [[int(x) - 1 for x in f.readline().split()] for _ in range(n)]

    zone = [0] * rows * cols
    zone[0] = 1
    max_zone = 1
    actual = [0, 1]

    print(f"entering main loop, t = {time.time() - start_time}")
    splits = [time.time()]
    for pos in range(rows * cols):
        paths = neighbors(pos, rows, cols, kind_map)
        splits += [time.time()]
        path_zones = {actual[zone[p]] for p in paths if zone[p]}
        splits += [time.time()]
        if not path_zones:
            max_zone += 1
            actual.append(max_zone)
            for p in paths:
                zone[p] = max_zone
        else:
            new = min(path_zones)
            while new != actual[new]:
                new = actual[new]
            for p in paths:
                if zone[p] != 0:
                    actual[zone[p]] = new
                zone[p] = new
        splits += [time.time()]

    update = [actual[x] for x in actual]
    while actual != update:
        actual = update
        update = [actual[x] for x in actual]
    actual = update

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
        if actual[zone[start]] == actual[zone[end]]:
            print(["binary", "decimal"][int(kind_map[start])])
        else:
            print("neither")

    diff = [splits[i] - splits[i-1] for i in range(1, len(splits))]
    a = sum(diff[0::3])
    b = sum(diff[1::3])
    c = sum(diff[2::3])
    print(a, b, c)


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
