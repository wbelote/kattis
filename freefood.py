#!/usr/bin/env python

import sys

def main(args):
    n = int(sys.stdin.readline())

    days = set()
    for i in range(n):
        line = sys.stdin.readline().split()
        for j in range(int(line[0]), int(line[1])+1):
            days.add(j)
    print(len(days))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
