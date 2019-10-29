import sys


def main():
    n = int(sys.stdin.readline())
    lines = []
    files = []
    compiled = []
    for i in range(n):
        line = sys.stdin.readline().split()
        child = line[0][:-1]
        if not line[1:]:
            compiled.append(child)
        lines.append(line[1:])
        files.append(child)

    needs = {h: {g: 0 for g in files} for h in files}
    for i in range(n):
        needs[files[i]]["total"] = len(lines[i])
        for p in lines[i]:
            needs[files[i]][p] = 1

    first = sys.stdin.readline().strip()
    compiled.remove(first)
    for c in compiled:
        del needs[c]
        files.remove(c)
        for f in files:
            needs[f]["total"] -= needs[f][c]
            del needs[f][c]
    queue = [first]
    while queue:
        new = queue.pop(0)
        if new not in needs:
            print(new)
            continue
        if needs[new]["total"]:
            queue.append(new)
            continue
        # go to compile new
        print(new)
        files.remove(new)
        for f in files:
            if needs[new][f] or not needs[f]["total"]:
                del needs[f]
                files.remove(f)
                for g in files:
                    needs[g]["total"] -= needs[g][f]
                    del needs[g][f]
                continue
            elif needs[f][new]:
                queue.append(f)
            needs[f]["total"] -= needs[f][new]
            del needs[f][new]
        del needs[new]


if __name__ == '__main__':
    main()
