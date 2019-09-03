import sys


def main():
    register = [0] * 10
    ram = [0] * 1000
    for i in range(1000):
        n = sys.stdin.readline()
        if len(n) < 3:
            break
        ram[i] = int(n)
    steps = 0
    pos = 0

    while True:
        cmd = ram[pos]
        steps += 1
        print("pos", pos)
        print("steps", steps)
        print("cmd", cmd)
        input()

        a, b, c = cmd // 100, (cmd // 10) % 10, cmd % 10
        if a == 1 or pos == 999:
            print(steps)
            return
        if a == 2:
            register[b] = c
        if a == 3:
            register[b] += c
            register[b] %= 1000
        if a == 4:
            register[b] *= c
            register[b] %= 1000
        if a == 5:
            register[b] = register[c]
        if a == 6:
            register[b] += register[c]
            register[b] %= 1000
        if a == 7:
            register[b] *= register[c]
            register[b] %= 1000
        if a == 8:
            register[b] = ram[register[c]]
        if a == 9:
            ram[register[c]] = register[b]
        if a == 0 and c:
            print(register)
            pos = register[register[b]] - 1

        pos += 1


main()
