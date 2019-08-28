import sys


def main():
    n = int(sys.stdin.readline())
    total = 0
    for i in range(n):
        line = sys.stdin.readline().strip()
        number = int(line[:-1])
        power = int(line[-1])
        total += number ** power

    print(total)


main()