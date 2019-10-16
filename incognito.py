import sys


def main():
    t = int(sys.stdin.readline())
    for test in range(t):
        n = int(sys.stdin.readline())
        categories = []
        categories_set = set()
        counts = {}
        for item in range(n):
            name, cat = sys.stdin.readline().split()
            if cat in categories_set:
                counts[cat] += 1
            else:
                categories_set.add(cat)
                categories.append(cat)
                counts[cat] = 2

        total = 1
        for c in categories:
            total *= counts[c]
        print(total - 1)


if __name__ == '__main__':
    main()
