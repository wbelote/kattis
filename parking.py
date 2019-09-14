import sys

prices = [0] + [int(x) for x in sys.stdin.readline().split()]
minutes = [0] * 100
for i in range(3):
    a, b = [int(x) for x in sys.stdin.readline().split()]
    for m in range(a, b):
        minutes[m] += 1

cost = [m * prices[m] for m in minutes]
print(sum(cost))
