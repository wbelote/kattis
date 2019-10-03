import sys


def main():
    t = int(sys.stdin.readline())
    for test in range(t):
        n = int(sys.stdin.readline())
        numbers = [sys.stdin.readline().rstrip() for i in range(n)]
        numbers.sort()
        consistent = True
        for i in range(1, n):
            if numbers[i].startswith(numbers[i - 1]):
                consistent = False
                break

        print(["NO", "YES"][consistent])


if __name__ == '__main__':
    main()
