import sys, math

def decode(line):
    out = ""
    n = int(math.sqrt(len(line)))
    for i in range(n-1, -1, -1):
        for j in range(n):
            out += line[j*n + i]
    return out

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        line = sys.stdin.readline()
        print(decode(line))

main()
##print(decode("RSTEEOTCP"))
##print(decode("eedARBtVrolsiesuAoReerles"))
##print(decode("EarSvyeqeBsuneMa"))
