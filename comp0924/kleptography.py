import sys, string


def num(c):
    return string.ascii_lowercase.index(c)


def letter(n):
    return string.ascii_lowercase[n]


def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    plain = sys.stdin.readline().rstrip()
    cipher = sys.stdin.readline().rstrip()
    # plain = ["" for i in range(m - n)] + list(end_s)

    for i in range(m - n):
        c = cipher[-1 - i]
        p = plain[-1 - i]
        char = num(c) - num(p)
        plain = letter(char) + plain

    print(plain)


main()
