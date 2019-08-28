import sys


def main():
    line = sys.stdin.readline().split()
    numbers = [int(n) for n in line]
    numbers.sort()
    letters = sys.stdin.readline()

    order = {"A": numbers[0], "B": numbers[1], "C": numbers[2]}

    print(order[letters[0]], order[letters[1]], order[letters[2]])


main()
