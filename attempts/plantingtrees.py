import sys

def main():
    n = int(sys.stdin.readline())
    line = sys.stdin.readline().split()
    trees = [int(t) for t in line]
    trees.sort()
    trees = trees[::-1]
    trees = [trees[i] + i + 1 for i in range(n)]
    print(max(trees)+1)    
    

main()
