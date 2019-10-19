import sys

cols = {"ABCDEFGH"[i]: i + 1 for i in range(8)}
names = " ABCDEFGH"


def are_diag(points):
    return abs(points[0] - points[2]) == abs(points[1] - points[3])


def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        line = sys.stdin.readline().split()
        path = [cols[line[0]], int(line[1]), cols[line[2]], int(line[3])]
        if sum(path) % 2:
            print("Impossible")
        elif path[0] == path[2] and path[1] == path[3]:
            print(f"0 {names[path[0]]} {path[1]}")
        elif are_diag(path):
            print(f"1 {names[path[0]]} {path[1]} {names[path[2]]} {path[3]}")
        else:
            xdiff = path[2] - path[0]
            ydiff = path[3] - path[1]
            a = [(xdiff + ydiff) // 2] * 2
            b = [xdiff - a[0], ydiff - a[1]]
            #print(xdiff, ydiff, a, b)
            if path[0] + a[0] in range(1, 9) and path[1] + a[1] in range(1, 9):
                mid = [path[0] + a[0], path[1] + a[1]]
            else:
                mid = [path[0] + b[0], path[1] + b[1]]
            print(f"2 {names[path[0]]} {path[1]} {names[mid[0]]} {mid[1]} {names[path[2]]} {path[3]}")


main()
