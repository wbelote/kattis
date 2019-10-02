import sys


def islands(data):
    if not data:
        return 0
    level = min(data)
    parts = [[]]
    for val in data:
        if val > level:
            parts[-1].append(val)
        elif parts[-1]:
            parts.append([])

    if parts == [[]]:
        return 0

    if len(parts) > 1 and parts[-1] == []:
        del parts[-1]

    total = 0
    for part in parts:
        total += islands(part)

    return total + len(parts)


def main():
    p = int(sys.stdin.readline())
    for i in range(p):
        line = sys.stdin.readline().split()
        stream = [int(x) for x in line[1:]]
        print(line[0], islands(stream))


if __name__ == '__main__':
    main()
