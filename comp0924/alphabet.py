import sys, itertools


def main():
    line = sys.stdin.readline().rstrip()
    for i in range(26, 0, -1):
        exists = False
        for sub in itertools.combinations(line, i):
            substr = [s for s in sub]
            if substr == sorted(substr):
                exists = True
                break
        if exists:
            print(26 - i)
            return


main()
