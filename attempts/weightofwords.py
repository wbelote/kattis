import sys

def main():
    letters = "abcdefghijklmnopqrstuvwxyz"
    line = sys.stdin.readline().split()
    l = int(line[0])
    w = int(line[1])

    if w > l * 25:
        print("impossible")
    else:
        a = w // 26
        mid = w % 26
        z = l - a - 1
        print('a'*a, letters[mid], 'z'*z, sep="")

main()
