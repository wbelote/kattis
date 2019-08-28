import sys

def main():
    line = sys.stdin.readline().split()
    h = int(line[0])
    m = int(line[1])
    
    m += 15
    h += m // 60
    m = m % 60
    h += 23
    h = h % 24
    
    print(h, m)

main()
