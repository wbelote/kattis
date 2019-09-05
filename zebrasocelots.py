import sys


def main():
    n = int(sys.stdin.readline())
    pile = [sys.stdin.readline()[0] for i in range(n)][::-1]

    count = 0
    while True:
        if "O" not in pile:
            print(count)
            return
        pos = pile.index("O")
        pile = ["O"] * pos + ["Z"] + pile


main()
