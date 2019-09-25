import sys, string


def crawl(ref, case, b=()):
    if not ref or not case:
        return b

    if ref[0] == case[0]:
        new = case[:]
        while ref[0] in new:
            new.remove(ref[0])
        return crawl(ref[1:], new, b + (ref[0],))

    new = case[:]
    i = 0
    while i < len(new):
        if new[i] <= case[0]:
            del new[i]
        else:
            i += 1

    take = crawl(ref[ref.index(case[0]):], new, b + (case[0],))
    leave = crawl(ref, case[1:], b)
    if len(take) > len(leave):
        return take
    else:
        return leave


def main():
    line = list(sys.stdin.readline().rstrip())
    alpha = list(string.ascii_lowercase)

    print(26 - len(crawl(alpha, line)))


main()
