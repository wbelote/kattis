import sys


def is_queue(data):
    queue = []
    for line in data:
        if line[0] == "1":
            queue.append(line[1])
        elif not queue:
            return -1
        elif queue.pop(0) != line[1]:
            return 0
    return 1


def is_stack(data):
    stack = []
    for line in data:
        if line[0] == "1":
            stack.append(line[1])
        elif not stack:
            return -1
        elif stack.pop() != line[1]:
            return 0
    return 1


def is_priority(data):
    priority = []
    for line in data:
        if line[0] == "1":
            priority.append(line[1])
        elif not priority:
            return -1
        elif max(priority) != line[1]:
            return 0
        else:
            priority.remove(max(priority))
    return 1


def main():
    cases = sys.stdin.readlines()
    while cases:
        n = int(cases.pop(0))
        data = [cases.pop(0).split() for _ in range(n)]
        possible = [is_stack(data), is_queue(data), is_priority(data)]
        if -1 in possible or sum(possible) < 1:
            print("impossible")
        elif sum(possible) > 1:
            print("not sure")
        else:
            print(["stack", "queue", "priority queue"][possible.index(1)])
    print()


if __name__ == '__main__':
    main()
