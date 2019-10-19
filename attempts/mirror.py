import sys


def main():
    t = int(sys.stdin.readline())
    for case in range(t):
        r, c = [int(x) for x in sys.stdin.readline().split()]
        image = []
        for i in range(r):
            image.append(sys.stdin.readline().rstrip()[::-1])

        print("Test", case+1)
        for row in image[::-1]:
            print("".join(row))


main()
