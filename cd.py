import sys


def main():
    while True:
        line = sys.stdin.readline().split()
        n, m = [int(x) for x in line]
        if not n + m:
            return
        if not n or not m:
            print(0)
            continue

        cds = [sys.stdin.readline() for i in range(n+m)]
        jack = set(cds[:n])
        jill = set(cds[n:])

        print(len(jack & jill))


main()