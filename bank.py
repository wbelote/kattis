import sys


def max_cash(data):
    """
    Finds the max total picking from options. It looks at all feasible options for this pick, and compares the
    best totals that that pick can result in. Ends up basically being a depth first search of a decision tree
    to find the highest path sum.
    :param data: input data where options[i] is a list of all values that expire after i minutes
    :return: highest possible total
    """
    # Default cases
    if data == [] or data == [[]]:
        return 0
    if len(data) == 1:
        return max(data[0])

    # Find all good options to serve at this time.
    # Values are only worth considering if they leave soon or are worth a lot.
    # We only consider the highest value at each leaving time (at least for this pick).
    # Starting with the soonest leaving time, we then add any later times with higher values.
    pick = []
    for i, val in enumerate(data):
        if val and not pick:
            pick = [i]
        elif val and val[-1] > data[pick[-1]][-1]:
            pick.append(i)

    # We then look at each option and find the max we can get if we take it.
    totals = []
    for p in pick:
        copy = [x[:] for x in data]
        take = copy[p].pop()
        for i in range(len(copy)):
            copy[i] = copy[i][-i:]
        totals.append(take + max_cash(copy[1:]))
    return max(totals)


def main():
    n, t = [int(x) for x in sys.stdin.readline().split()]

    # Store data as the cash options that leave at 0, that leave at 1, etc.
    # people[i] is a list of all cash values that leave after i minutes.
    people = [[] for _ in range(t)]
    for i in range(n):
        cash, wait = [int(x) for x in sys.stdin.readline().split()]
        people[wait] += [cash]

    # We can only get max 1 value that leaves at 0, max 2 that leave at 1, etc.
    for i in range(t):
        people[i].sort()
        people[i] = people[i][:i + 1]

    # If there are later minutes where everyone has left, we can ignore them
    while not people[-1]:
        people = people[:-1]

    # Use recursive algorithm to find the max
    print(max_cash(people))


if __name__ == '__main__':
    main()
