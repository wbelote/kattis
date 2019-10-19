import sys

dom = {"A": 11, "K": 4, "Q": 3, "J": 20, "T": 10, "9": 14, "8": 0, "7": 0}
non = {"A": 11, "K": 4, "Q": 3, "J": 2, "T": 10, "9": 0, "8": 0, "7": 0}

n, d = sys.stdin.readline().split()
cards = [sys.stdin.readline() for i in range(int(n) * 4)]
print(sum(
    [int([non, dom][int(c[1] == d)][c[0]]) for c in cards]
))
