import sys

def main():
    n = int(sys.stdin.readline())
    line = sys.stdin.readline().split()
    stops = [int(s) for s in line]
    stops.sort()
    
    out = []
    i = 0
    while True:
        
        for j in range(i, n):
            if j == n-1:
                if j == i:
                    out.append(str(stops[i]))
                if j == i+1:
                    out.append(str(stops[i]))
                    out.append(str(stops[j]))
                if j >= i+2:
                    out.append(f"{stops[i]}-{stops[j]}")
                print(" ".join(out))
                return
            if stops[j+1] - stops[j] > 1:
                # done with this range
                if j == i:
                    out.append(str(stops[i]))
                if j == i+1:
                    out.append(str(stops[i]))
                    out.append(str(stops[j]))
                if j >= i+2:
                    out.append(f"{stops[i]}-{stops[j]}")
                i = j + 1
                break

main()
