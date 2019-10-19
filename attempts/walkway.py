import sys


def price(stone):
    return 0.01 * stone[2] * (stone[0]+stone[1])


def walkway(start, finish, stones):
    if start == finish:
        return 0
    fits = []
    i = 0
    while stones and i < len(stones):
        if len(stones[i]) != 3:
            print(stones[i])
            raise IndexError
        if start in stones[i][:2] and stones[i][0] != stones[i][1]:
            fits.append(stones.pop(i))
        else:
            i += 1

    prices = []
    for stone in fits:
        if stone[:2] in [[start, finish], [finish, start]]:
            prices.append(price(stone))
        elif stone[0] == start:
            stones2 = [s[:] for s in stones]
            remaining = walkway(stone[1], finish, stones2)
            if remaining:
                prices.append(price(stone) + remaining)
        else:
            stones2 = [s[:] for s in stones]
            remaining = walkway(stone[0], finish, stones2)
            if remaining:
                prices.append(price(stone) + remaining)

    if prices:
        return min(prices)
    return -1


def main():
    n = int(sys.stdin.readline())
    while n:
        stones = []
        for i in range(n):
            line = sys.stdin.readline().split()
            stones.append([int(x) for x in line])

        start, finish = [int(x) for x in sys.stdin.readline().split()]
        print(walkway(start, finish, stones))
        n = int(sys.stdin.readline())


main()
