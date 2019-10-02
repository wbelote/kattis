import sys


def four(x):
    ops = ["+", "-", "*", "//"]
    for a in ops:
        for b in ops:
            for c in ops:
                exp = f"4 {a} 4 {b} 4 {c} 4"
                res = int(eval(exp))
                if res == x:
                    return f"{exp} = {res}".replace("//", "/")
    return "no solution"


m = int(sys.stdin.readline())
for i in range(m):
    n = int(sys.stdin.readline())
    print(four(n))