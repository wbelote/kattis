import sys


def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        turtles = [int(x) for x in sys.stdin.readline().split()]
        total = 0
        for year in range(1, len(turtles)):
            diff = turtles[year] - turtles[year - 1] * 2
            total += diff * int(diff > 0)
        print(total)


main()
