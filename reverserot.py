import sys

def rotate(c, n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    return letters[(letters.index(c)+n) % 28]

def main():
    while True:
        line = sys.stdin.readline().split()
        if line[0] == "0":
            return
        n = int(line[0])
        s = line[1][::-1]
        for char in s:
            print(rotate(char, n), end="")
        print()

main()
