import sys


def main():
    n = int(sys.stdin.readline())
    edges = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
    path = [0, 1]
    dist = edges[0][1]
    for i in range(2, n):
        front = edges[path[0]][i]
        back = edges[path[-1]][i]
        if front < back:
            path = [i] + path
            dist += front
        else:
            path += [i]
            dist += back
    print(dist)


if __name__ == '__main__':
    main()
