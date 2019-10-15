import sys


def main():
    t = int(sys.stdin.readline())
    for test in range(t):
        n = int(sys.stdin.readline())
        possible_ingredients = {}
        seen = set()
        for pizza in range(n):
            pizza_name = sys.stdin.readline()
            foreign = sys.stdin.readline().split()[1:]
            native = set(sys.stdin.readline().split()[1:])
            for ingredient in foreign:
                if ingredient in seen:
                    possible_ingredients[ingredient] &= native
                else:
                    seen.add(ingredient)
                    possible_ingredients[ingredient] = native.copy()

        for name in sorted(list(seen)):
            possible = list(possible_ingredients[name])
            for trans in sorted(possible):
                print(f"({name}, {trans})")
        print()


if __name__ == '__main__':
    main()
