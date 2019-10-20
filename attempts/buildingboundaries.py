import sys


def combine(nums):
    possible = []
    for a in range(2):
        for b in range(2):
            possible.append([nums[0] + nums[2], max(nums[1::2])])
            nums[2], nums[3] = nums[3], nums[2]
        nums[0], nums[1] = nums[1], nums[0]


def main():
    tests = int(sys.stdin.readline())
    for t in range(tests):
        a1, b1, a2, b2, a3, b3 = [int(n) for n in sys.stdin.readline().split()]
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

        print(best)


if __name__ == '__main__':
    main()

