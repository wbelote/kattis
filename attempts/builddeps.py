import sys


def main():
    n = int(sys.stdin.readline())
    children = {}
    parents = {}
    compiled = set()
    for i in range(n):
        line = sys.stdin.readline().split()
        child = line[0][:-1]
        parents[child] = line[1:]
        if not parents[child]:
            compiled.add(child)
        for file in line[1:]:
            if file in children:
                children[file] += [child]
            else:
                children[file] = [child]

    queue = [sys.stdin.readline().rstrip()]
    compiled.remove(queue[0])
    while queue:
        item = queue.pop(0)
        if item in compiled:
            continue
        if not set(parents[item]) <= compiled:
            queue.append(item)
            continue
        else:
            compiled.add(item)
            print(item)
            if item in children:
                queue += children[item]


if __name__ == '__main__':
    main()
