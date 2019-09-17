import sys


def insort(n, names):
    if not names:
        return [n]
    lo = 0
    hi = len(names) - 1
    while True:
        guess = (lo+hi) // 2
        if names[guess][:2] <= n[:2]:
            return names[:guess+1] + insort(n, names[guess+1:])
        else:
            return insort(n, names[:guess]) + names[guess:]


def main():
    n = int(sys.stdin.readline())
    while n:
        names = []
        for i in range(n):
            name = sys.stdin.readline().rstrip()
            names = insort(name, names)

        print("\n".join(names))
        print()

        n = int(sys.stdin.readline())


main()
