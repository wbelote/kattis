import sys


def search(n):
    ops = [" + ", " - ", " * ", " / "]

    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                exp = "4" + op1 + "4" + op2 + "4" + op3 + "4"
                val = None
                exec(f"val = {exp}")
                print(f"val = {exp}")
                print(exp, val)
                if val == n:
                    return exp

    return "no solution"


def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        line = int(sys.stdin.readline())
        print(search(line))


main()
