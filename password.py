import sys


def main():
    n = int(sys.stdin.readline())
    passwords = []
    for i in range(n):
        p = float(sys.stdin.readline().split()[1])
        passwords.append(p)
    passwords.sort()
    total = 0
    for i in range(1, n + 1):
        p = passwords[-i]
        total += i * p
    print(total)


if __name__ == '__main__':
    main()
