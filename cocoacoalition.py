import sys

def find_snaps(m, n, a):
    print(m,n,a)
    if 0 in {m, n}:
        return 0
    if m * n - a < a:
        a = m * n - a
    if 0 in {a % m, a % n}:
        return 1
    if a < m or a < n:
        return 2

    if  a//n > a//m:
        new_a = a % n
        n = n - (a//n)
    else:
        new_a = a % m
        m = m - (a//m)

    return find_snaps(m, n, new_a) + 1


n, m, a = [int(x) for x in sys.stdin.readline().split()]
print(find_snaps(m, n, a))
