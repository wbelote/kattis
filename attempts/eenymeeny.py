import sys

rhyme = sys.stdin.readline().split()
steps = len(rhyme) - 1
n = int(sys.stdin.readline())
kids = []
for k in range(n):
    kids.append(sys.stdin.readline().rstrip())

teams = [[], []]
chosen = 0
for k in range(n):
    chosen = (chosen + steps) % len(kids)
    teams[k % 2].append(kids.pop(chosen))

for t in (0, 1):
    print(len(teams[t]))
    for k in teams[t]:
        print(k)
