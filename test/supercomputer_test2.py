import time, bisect


def main():
    with open("supercomputer-input.txt", "r") as f:
        text = f.read().split("\n")

    splits = [time.time()]
    line = text[0].split()
    n, k = [int(x) for x in line]

    trues = []
    trues_set = set()
    queries = text[1:]

    print("Generated, running queries")
    splits.append(time.time())

    for i in range(k):
        if i % 10000 == 0:
            print(i // 10000)
        if i == k // 2:
            print("Halfway")
            splits.append(time.time())
        parts = queries[i].split()
        if parts[0] == "F":
            bit = int(parts[1])
            if bit in trues_set:
                trues.remove(bit)
                trues_set.remove(bit)
            else:
                trues_set.add(bit)
                trues.append(bit)
                trues.sort()
                # bisect.insort(trues, bit)
        if parts[0] == "C":
            # print(queries[i])
            start = int(parts[1])
            stop = int(parts[2])
            count = bisect.bisect_right(trues, stop) - bisect.bisect_left(trues, start)
            # print(count)

    print("Done")
    splits.append(time.time())
    print([splits[i + 1] - splits[i] for i in range(3)])


main()
