import sys

def check(line):
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    if a + b == c:
        return "Possible"
    if a - b == c or b - a == c:
        return "Possible"
    if a * b == c:
        return "Possible"
    if a / b == c or b / a == c:
        return "Possible"
    return "Impossible"

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        line = sys.stdin.readline()
        print(check(line))

main()
