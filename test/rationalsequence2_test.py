import sys

p = int(sys.stdin.readline())
line = [[1, 1]]
for i in range(p):
    new = []
    for j in range(len(line)):
        nxt = [[line[j][0], sum(line[j])], [sum(line[j]), line[j][1]]]
        print(f"{nxt[0][0]}/{nxt[0][1]} {nxt[1][0]}/{nxt[1][1]}", end=" ")
        new += nxt
    line = [x[:] for x in new]
    print()
