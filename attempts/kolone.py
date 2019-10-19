import sys


def main():
    a_len, b_len = [int(x) for x in sys.stdin.readline().split()]
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()
    t = int(sys.stdin.readline())
    rows = [1 for _ in range(a_len)] + [2 for _ in range(b_len)]
    seq = list(a[::-1] + b)
    row = {seq[j]: rows[j] for j in range(a_len + b_len)}

    for sec in range(t):
        new = seq[:]
        for i in range(1, a_len + b_len):
            if row[seq[i - 1]] < row[seq[i]]:
                new[i-1], new[i] = seq[i], seq[i - 1]
        seq = new
    print("".join(seq))


if __name__ == '__main__':
    main()
