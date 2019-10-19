import sys


def plot_sort(plot):
    for i in (0, 2, 4):
        if plot[i] < plot[i + 1]:
            plot[i], plot[i + 1] = plot[i + 1], plot[i]

    if plot[0:2] < plot[2:4]:
        plot[0:4] = plot[2:4] + plot[0:2]
    if plot[2:4] < plot[4:6]:
        plot[2:6] = plot[4:6] + plot[2:4]
    if plot[0:2] < plot[2:4]:
        plot[0:4] = plot[2:4] + plot[0:2]
    return plot


def main():
    tests = int(sys.stdin.readline())
    for t in range(tests):
        dims = [int(n) for n in sys.stdin.readline().split()]
        a, b, c, d, e, f = plot_sort(dims)

        options = [
            a * (b + d + f),
            max(a, c + e) * (b + max(d, f)),
            max(a, c + f) * (b + max(d, e)),
            max(a, d + f) * (b + max(c, e)),
            (a + f) * max(e, b + d),
            (a + d) * max(c, b + f),
            (a + c + e) * max(b, d, f),
            (a + c + f) * max(b, d, e),
            (a + d + f) * max(b, c, e),
            (a + max(c, e)) * max(b, d + f),
            (a + max(d, e)) * max(b, c + f),
            (a + max(d, f)) * max(b, c + e),
        ]
        print(min(options))


if __name__ == '__main__':
    main()
