import sys

n, m = sys.stdin.readline().split()
n, m = int(n), int(m)

outcomes = [0] * (n + m)
for i in range(n):
    for j in range(m):
        outcomes[i + j + 1] += 1

for i in range(outcomes.count(max(outcomes))):
    print(outcomes.index(max(outcomes)) + 1)
    outcomes[outcomes.index(max(outcomes))] = 0
