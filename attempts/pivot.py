import sys
import bisect


def main():
    n = int(sys.stdin.readline())
    nums = [int(x) for x in sys.stdin.readline().split()]
    total = 0
    max_so_far = nums[0] - 1
    possible = []
    for i in range(n):
        if nums[i] >= max_so_far:
            max_so_far = nums[i]
            bisect.insort(possible, nums[i])
            total += 1
        else:
            cut = bisect.bisect_right(possible, nums[i])
            possible = possible[:cut]
            total = cut

    print(total)


if __name__ == '__main__':
    main()
