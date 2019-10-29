import sys
import math


def y(x, l, w):
    return (w ** 2 - w ** 2 * x ** 2 / l ** 2) ** 0.5


def a(x, l, w):
    return math.pi * y(x, l, w) ** 2


def area(x, l, w):
    return math.pi * (x * w ** 2 - (w ** 2 * x ** 3) / (3 * l ** 2))


def main():
    potatoes = int(sys.stdin.readline())
    for p in range(1, potatoes + 1):
        print(f"Potato {p}")
        line = sys.stdin.readline().split()
        l = float(line[0]) / 2
        w = float(line[1]) / 2
        n = int(line[2])
        areas = [area((2 * l * i) / n - l, l, w) for i in range(n + 1)]
        slices = [areas[i + 1] - areas[i] for i in range(n)]
        for s in range(n):
            slice_area = "%0.3f" % slices[s]
            print(f"  Slice {s + 1} = {slice_area}")


if __name__ == '__main__':
    # for i in range(-2, 3):
    #     print(area(i, 2, 1))
    main()
