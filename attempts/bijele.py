import sys

def main():
    line = sys.stdin.readline().split()
    correct = [1, 1, 2, 2, 2, 8]
    
    for i in range(6):
        print(correct[i] - int(line[i]), end=" ")

main()
