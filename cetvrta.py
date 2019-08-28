import sys

def main():
    xs = []
    ys = []
    for i in range(3):
        x, y = sys.stdin.readline().split()
        if x in xs:
            xs.remove(x)
        else:
            xs.append(x)
        if y in ys:
            ys.remove(y)
        else:
            ys.append(y)
        
    print(xs[0], ys[0])

main()
        
