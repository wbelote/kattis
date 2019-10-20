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


def combine(nums):
    possible = []
    for a in range(2):
        for b in range(2):
            possible.append([nums[0] + nums[2], max(nums[1::2])])
            nums[2], nums[3] = nums[3], nums[2]
        nums[0], nums[1] = nums[1], nums[0]


def solve_old(dims):
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
    return min(options)


def solve_new(dims):
    a1, b1, a2, b2, a3, b3 = dims
    best = (a1 + a2 + a3) * (b1 + b2 + b3)

    for i in range(8):
        v1 = max(a1, a2 + a3) * (b1 + max(b2, b3))
        v2 = max(a2, a3 + a1) * (b2 + max(b3, b1))
        v3 = max(a3, a1 + a2) * (b3 + max(b1, b2))
        h = max(a1, a2, a3) * (b1 + b2 + b3)
        best = min(best, v1, v2, v3, h)

        a1, b1, = b1, a1
        if i % 2 == 1:
            a2, b2 = b2, a2
        if i % 4 == 3:
            a3, b3 = b3, a3

    return best


def main():
    tests = int(sys.stdin.readline())
    for t in range(tests):
        dims = [int(n) for n in sys.stdin.readline().split()]
        o = solve_old(dims)
        n = solve_new(dims)
        if o != n:
            print(dims)
            print(o, n)


if __name__ == '__main__':
    main()
