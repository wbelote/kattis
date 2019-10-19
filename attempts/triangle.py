import sys
import math


def main():
    case = 0
    for line in sys.stdin.readlines():
        case += 1
        n = int(line)
        if n == 0:
            print(f"Case {case}: 1")
        else:
            triangles = 3 ** (n + 1)
            size = 2 ** n
            t_dig = int(math.log10(triangles)) + 1
            s_dig = int(math.log10(size)) + 1
            print(f"Case {case}: {t_dig - s_dig}")


if __name__ == '__main__':
    main()
