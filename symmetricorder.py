import sys


def main():
    count = 0
    while True:
        count += 1
        n = int(sys.stdin.readline())
        if n == 0:
            return
        print("SET", count)

        names = [sys.stdin.readline().strip() for i in range(n)]
        names = names[::2] + names[1::2][::-1]
        for name in names:
            print(name)


main()
