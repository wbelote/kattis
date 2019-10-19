import sys


def pair(socks):
    if len(socks) <= 1:
        return 0
    for i in range(1, len(socks)):
        if socks[i] == socks[i - 1]:
            return i
    return 0


def main():
    n = int(sys.stdin.readline())
    orig = [int(x) for x in sys.stdin.readline().split()][::-1]
    aux = []

    moves = 0
    while True:
        if not orig and not aux:
            return moves

        if orig and aux and orig[-1] == aux[-1]:
            orig.pop()
            aux.pop()
            moves += 1
            continue

        o = pair(orig[::-1])
        a = pair(aux)
        moves += 1
        if 0 < o <= a or (o and not a):
            aux.append(orig.pop())
        elif 0 < a <= o or (a and not o):
            orig.append(aux.pop())
        else:
            return "impossible"


if __name__ == '__main__':
    print(main())
