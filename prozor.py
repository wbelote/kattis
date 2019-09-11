import sys


def main():
    line = sys.stdin.readline().split()
    r, s, k = [int(x) for x in line]
    # R lines contain S characters, racket is K*K
    picture = []
    for i in range(r):
        picture.append(sys.stdin.readline().rstrip())

    max_count = 0
    max_x = 0
    max_y = 0
    for y in range(r - k + 1):
        for x in range(s - k + 1):
            count = sum([line[x+1:x+k-1].count("*") for line in picture[y+1:y+k-1]])
            # print(x, y, count)
            # print(x+1, x+k-1, y+1, y+k-1)
            # print([line[x+1:x+k-1] for line in picture[y+1:y+k-1]])
            if count > max_count:
                max_count, max_x, max_y = count, x, y
            # print()

    print(max_count)
    for row in range(r):
        for col in range(s):
            if row in (max_y, max_y + k - 1) and col in (max_x, max_x + k - 1):
                print("+", end="")
            elif row in (max_y, max_y + k - 1) and max_x < col < max_x + k - 1:
                print("-", end="")
            elif max_y < row < max_y + k - 1 and col in (max_x, max_x + k - 1):
                print("|", end="")
            else:
                print(picture[row][col], end="")
        print()


main()
