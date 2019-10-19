import sys

def process(line):
    return sum([int(x) for x in line])


scores = [process(sys.stdin.readline().split()) for i in range(5)]

print(scores.index(max(scores)), max(scores))