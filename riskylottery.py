import sys, itertools


def winner(r):
    r.sort()
    for x in r:
        if r.count(x) == 1:
            return x

    return -1


def prob_win(r, n, m, weights):
    p_solo = (1 - 1 / m) ** n - 1



def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]

    weights = [0] * m

    winners = [0, 0, 0, 0, 0, 0, 0, 0]
    for result in itertools.product([1, 2, 3], repeat=3):
        w = winner(list(result))
        winners[w - 1] += int(result[0] == w)

    print(winners)


main()
