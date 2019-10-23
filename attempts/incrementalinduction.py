import sys


def main():
    n = int(sys.stdin.readline())
    won_game = [[0] * n for _ in range(n)]
    beaten_by = [[x] for x in range(n)]
    win_count = [0] * n
    for i in range(1, n):
        line = sys.stdin.readline()
        for j in range(i):
            if line[j] == "1":
                won_game[i][j] = won_game[j][i] = 1
                beaten_by[i] += [j]
                win_count[i] += 1
            else:
                won_game[i][j] = won_game[j][i] = -1
                beaten_by[j] += [i]
                win_count[j] += 1

    rotate = [line[:] for line in won_game]
    min_rot = [0, 0]
    for j in range(1, n):
        for i in range(j):
            rotate[i][j] += rotate[i][j - 1]
            if rotate[i][j] < rotate[min_rot[0]][min_rot[1]]:
                min_rot = rotate[i][j]
            rotate[-1 - i][-1 - j] += rotate[-1 - i][-j]
            if rotate[-1 - i][-1 - j] < rotate[min_rot[0]][min_rot[1]]:
                min_rot = rotate[-1 - i][-1 - j]

    if rotate[min_rot[0]][min_rot[1]]:
        


if __name__ == '__main__':
    main()
