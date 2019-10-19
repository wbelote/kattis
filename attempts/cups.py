import sys

def main():
    n = int(sys.stdin.readline())
    cups = {}
    for i in range(n):
        line = sys.stdin.readline().split()
        if line[0].isalpha():
            cups[int(line[1])] = line[0]
        else:
            cups[int(line[0])//2] = line[1]

    while len(cups):
        print(cups.pop(min(cups)))


main()
