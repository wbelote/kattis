import sys


def main():
    t = int(sys.stdin.readline())
    for case in range(t):
        n = int(sys.stdin.readline())
        people = []
        for person in range(n):
            line = sys.stdin.readline().split()
            name = line[0].strip(":")
            cl = line[1].split("-")
            cl_n = 0
            i = 9
            while cl:
                cl_n += {"upper": -1, "middle": 0, "lower": 1}[cl.pop()] * 3 ** i
                i -= 1
            people += [[cl_n, name]]
        people.sort()
        for p in people:
            print(p[1])
        print("=" * 30)


if __name__ == '__main__':
    main()
