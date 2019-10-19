import sys


def slope(a, b):
    return (b[1] - a[1]) / (b[0] - a[0])


def intersect(m1, b1, m2, b2):
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return [x, y]


def line_mb(a, b):
    m = slope(a, b)
    b = a[1] - m * a[0]
    return [m, b]


def ext(a, b, c):
    midpoint = [(a[i] + b[i]) / 2 for i in range(2)]
    if a[1] == b[1]:
        end_m = -1 / slope(b, c)
        end_b = b[1] - end_m * b[0]
        x = midpoint[0]
        y = end_m * x + end_b
        return [x, y]
    if b[1] == c[1]:
        mid_m = -1 / slope(a, b)
        mid_b = midpoint[1] - mid_m * midpoint[0]
        x = b[0]
        y = mid_m * x + mid_b
        return [x, y]
    if a[0] == b[0]:
        mid_m = 0
    else:
        mid_m = -1 / slope(a, b)
    mid_b = midpoint[1] - mid_m * midpoint[0]
    if b[0] == c[0]:
        end_m = 0
    else:
        end_m = -1 / slope(b, c)
    end_b = b[1] - end_m * b[0]
    return intersect(mid_m, mid_b, end_m, end_b)


def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        line = sys.stdin.readline().split()
        k = int(line[0])
        a, b, c = [(float(line[i]), float(line[i + 1])) for i in (1, 3, 5)]

        ext_ab = ext(a, b, c)
        ext_bc = ext(b, c, a)

        if ext_ab[0] == ext_bc[0]:
            x = ext_ab[0] * 2 - b[0]
            y = b[1]
        elif ext_ab[1] == ext_bc[1]:
            x = b[0]
            y = ext_ab[1] * 2 - b[1]
        else:
            mirror_m, mirror_b = line_mb(ext_ab, ext_bc)
            perp_m = -1 / slope(ext_ab, ext_bc)
            perp_b = b[1] - perp_m * b[0]
            mid_x, mid_y = intersect(mirror_m, mirror_b, perp_m, perp_b)
            x = mid_x * 2 - b[0]
            y = mid_y * 2 - b[1]

        print(k, x, y)


main()
