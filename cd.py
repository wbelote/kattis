import sys

def main():
    n = sys.stdin.readline().split()
    jack = []
    jill = []
    
    for i in range(int(n[0])):
        jack.append(int(sys.stdin.readline()))
        
    for i in range(int(n[1])):
        jill.append(int(sys.stdin.readline()))

    both = 0
    for cd in set(jack+jill):
        if cd in jack and cd in jill:
            both += 1
    print(both)
        

main()
