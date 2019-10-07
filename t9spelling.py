import sys

t9 = [
    "2", "22", "222",
    "3", "33", "333",
    "4", "44", "444",
    "5", "55", "555",
    "6", "66", "666",
    "7", "77", "777", "7777",
    "8", "88", "888",
    "9", "99", "999", "9999",
    "0",
]
letters = "abcdefghijklmnopqrstuvwxyz "


def main():
    n = int(sys.stdin.readline())
    for case in range(1, n + 1):
        line = sys.stdin.readline().rstrip()
        out = f"Case #{case}: "
        for char in line:
            new = t9[letters.index(char)]
            if new[0] == out[-1]:
                out += " "
            out += new
        print(out)


main()
