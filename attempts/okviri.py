import sys


def main():
    line = sys.stdin.readline().rstrip()
    out = [["." for i in range(1 + 4 * len(line))] for j in range(5)]
    for i in range(len(line)):
        col = 2 + 4 * i
        out[0][col] = "#"
        out[1][col - 1] = "#"
        out[1][col + 1] = "#"
        out[2][col - 2] = "#"
        out[2][col] = line[i]
        out[2][col + 2] = "#"
        out[3][col - 1] = "#"
        out[3][col + 1] = "#"
        out[4][col] = "#"

    for i in range(2, len(line), 3):
        col = 2 + 4 * i
        out[0][col] = "*"
        out[1][col - 1] = "*"
        out[1][col + 1] = "*"
        out[2][col - 2] = "*"
        out[2][col] = line[i]
        out[2][col + 2] = "*"
        out[3][col - 1] = "*"
        out[3][col + 1] = "*"
        out[4][col] = "*"

    for i in range(5):
        print("".join(out[i]))


main()
