import sys


def main():
    start = sys.stdin.readline().rstrip()
    parent = {}
    line = sys.stdin.readline().split()
    while line[0] != "-1":
        for i in range(1, len(line)):
            parent[line[i]] = line[0]
        line = sys.stdin.readline().split()

    path = [start]
    while path[-1] in parent.keys():
        path.append(parent[path[-1]])

    print(" ".join(path))


main()
