import sys


def count_in(sub, string):
    if len(sub) >= len(string):
        return int(sub == string)
    if sub[0] not in string:
        return 0
    start = string.index(sub[0]) + 1
    return count_in(sub[1:], string[start:]) + count_in(sub, string[start:])


def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        line = sys.stdin.readline().strip()
        n = count_in("welcome to code jam", line)

        print(f"Case #{i + 1}: {str.zfill(str(n), 4)}")


main()
