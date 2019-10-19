import sys


def prob(data, adjust=None):
    if adjust is not None and data[adjust] > 0:
        data[adjust] -= 1
    if data[4] <= 0:
        return 0.0
    if max(data[:4]) <= 0:
        return 1.0

    total = [prob(data[:], data.index(max(data[:4])))]
    for i in range(5):
        if data[i]:
            total += [prob(data[:], i)]
    return sum(total) / len(total)


def main():
    line = [int(x) for x in sys.stdin.readline().split()]
    print(prob(line))


if __name__ == '__main__':
    main()
