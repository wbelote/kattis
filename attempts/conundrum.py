import sys

line = sys.stdin.readline().strip()

print(sum([int(line[i] != "PER"[i % 3]) for i in range(len(line))]))