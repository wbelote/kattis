import sys

n = int(sys.stdin.readline())
days = [int(x) for x in sys.stdin.readline().split()]

min_temp = max(days) + 1
min_day = -1

for d in range(2, n):
    # print(d, days[d], d - 2, days[d - 2])
    # print(min_day, min_temp)
    if max([days[d], days[d - 2]]) < min_temp:
        min_day = d - 1
        min_temp = max([days[d], days[d - 2]])

print(min_day, min_temp)
