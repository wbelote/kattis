import sys

n = int(sys.stdin.readline())
for case in range(1, n + 1):
    r, c = [int(x) for x in sys.stdin.readline().split()]
    lines = [[x for x in sys.stdin.readline().split()] for _ in range(r)]

    print(f"T of Matrix {case}:")
    for i in range(c):
        row = [lines[j][i] for j in range(r)]
        print(" ".join(row))
    print()
