import sys


def main():
    n = int(sys.stdin.readline())
    e = int(sys.stdin.readline())
    heard = [set() for _ in range(n + 1)]
    songs = 0
    for evening in range(e):
        present = [int(x) for x in sys.stdin.readline().split()[1:]]
        if 1 in present:
            for v in present:
                heard[v].add(songs)
            songs += 1
        else:
            there = set()
            for v in present:
                there |= heard[v]
            for v in present:
                heard[v] |= there

    heard_all = [1]
    for i in range(2, n + 1):
        if heard[1] == heard[i]:
            heard_all += [i]
    for v in heard_all:
        print(v)


if __name__ == '__main__':
    main()
