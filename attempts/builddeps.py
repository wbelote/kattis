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
        if len(line) == 1:
            compiled.add(child)
        for file in line[1:]:
            if file in children:
                children[file] += [child]
            else:
                children[file] = [child]

    queue = [sys.stdin.readline().rstrip()]
    needs_compiling = {queue[0]}
    compiled.remove(queue[0])
    while queue:
        item = queue.pop(0)
        if item in compiled:
            continue
        for p in parents[item]:
            if p not in compiled:
                queue.append(item)
                continue
        compiled.add(item)
        needs_compiling.remove(item)
        print(item)
        if item in children:
            needs_compiling |= set(children[item])
            queue += children[item]


if __name__ == '__main__':
    main()
