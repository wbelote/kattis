import sys

n = int(sys.stdin.readline())

for i in range(n):
    sys.stdin.readline()
    guests = sys.stdin.readline().split()
    codes = set()
    for g in guests:
        codes ^= {g}
    print(f"Case #{i+1}:", codes.pop())
