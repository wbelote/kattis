import sys

n, m, k = [int(x) for x in sys.stdin.readline().split()]

if m > n:
    m = n

h = (n - m) // k
small = (m - 1) * (m / 2)
big = (h + 1) * (n - (k * (h / 2)))

print(int(big + small))
