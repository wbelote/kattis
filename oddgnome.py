import sys

n = int(sys.stdin.readline())
for i in range(n):
    gnomes = [int(x) for x in sys.stdin.readline().split()]
    for g in range(2, gnomes[0]):
        if gnomes[g + 1] - gnomes[g - 1] == 1:
            print(g)
