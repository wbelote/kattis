import sys


def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    connections = {i: set() for i in range(1, n + 1)}
    for i in range(m):
        a, b = [int(x) for x in sys.stdin.readline().split()]
        connections[a].add(b)
        connections[b].add(a)
    without = list(range(1, n + 1))
    internet = set()
    add = {1}
    while add:
        house = add.pop()
        without.remove(house)
        add |= connections[house] - internet
        internet.add(house)
    if without:
        for h in without:
            print(h)
    else:
        print("Connected")


if __name__ == '__main__':
    main()
