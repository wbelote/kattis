import sys


def main():
    n = int(sys.stdin.readline())

    for i in range(n):
        a = sys.stdin.readline().strip()
        b = sys.stdin.readline().strip()
        diff = ""
        for j in range(len(a)):
            diff += ["*", "."][a[j] == b[j]]

        print(a)
        print(b)
        print(diff)


main()
