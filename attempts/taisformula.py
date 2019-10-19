import sys


def main():
    n = int(sys.stdin.readline())
    t = []
    v = []
    for i in range(n):
        line = sys.stdin.readline().split()
        t.append(int(line[0]))
        v.append(float(line[1]))

    total = 0
    for i in range(1, n):
        total += ((v[i] + v[i - 1]) / 2) * (t[i] - t[i - 1])

    print(total / 1000)


main()
