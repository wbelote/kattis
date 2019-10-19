import sys, bisect


def insert(x, nums):
    if len(nums) == 0:
        return [x]
    if len(nums) <= 1:
        return [min(nums + [x]), max(nums + [x])]
    mid = len(nums) // 2
    if x < nums[mid-1]:
        mid -= 1
        return insert(x, nums[:mid]) + nums[mid:]
    elif x > nums[mid]:
        return nums[:mid] + insert(x, nums[mid:])
    else:
        return nums[:mid] + [x] + nums[mid:]


def get_index(x, nums):
    if len(nums) == 0:
        return 0
    lower = 1
    upper = len(nums)
    if x <= nums[0]:
        return 0
    if x > nums[-1]:
        return upper

    while True:
        guess = (lower + upper) // 2
        # print("guess:", guess)
        if nums[guess - 1] < x <= nums[guess]:
            return guess
        if nums[guess] > x:
            upper = guess
        else:
            lower = guess


def main():
    line = sys.stdin.readline().split()
    n, k = [int(x) for x in line]

    trues = []
    trues_set = set()

    for i in range(k):
        parts = sys.stdin.readline().split()
        if parts[0] == "F":
            bit = int(parts[1])
            if bit in trues_set:
                trues.remove(bit)
                trues_set.remove(bit)
            else:
                trues_set.add(bit)
                bisect.insort(trues, bit)
        if parts[0] == "C":
            start = int(parts[1])
            stop = int(parts[2])
            count = bisect.bisect_right(trues, stop) - bisect.bisect_left(trues, start)
            print(count)


main()
