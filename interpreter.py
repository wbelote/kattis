import sys


def main():
    register = ['000'] * 10
    ram = [sys.stdin.readlines() for i in range(15)]
    ram += ['000'] * (1000 - len(ram))
    steps = 0
    pos = 0

    while True:
        cmd = ram[pos]
        steps += 1
        print(steps)

        if cmd[0] == "1":
            print(steps)
            return
        if cmd[0] == "2":
            d, n
            register[int(cmd[1])] = "00" + cmd[2]
        if cmd[0] == "3":
            register[int(cmd[1])] = str(int(register[int(cmd[1])]) + int(cmd[2]))[:3]
        if cmd[0] == "4":
            register[int(cmd[1])] = str(int(register[int(cmd[1])]) * int(cmd[2]))[:3]
        if cmd[0] == "5":
            register[int(cmd[1])] = register[int(cmd[2])]
        if cmd[0] == "6":
            register[int(cmd[1])] = str(int(register[int(cmd[1])]) + int(register[int(cmd[2])]))[:3]
        if cmd[0] == "7":
            register[int(cmd[1])] = str(int(register[int(cmd[1])]) * int(register[int(cmd[2])]))[:3]
        if cmd[0] == "8":
            register[int(cmd[1])] = ram[int(register[int(cmd[2])])]
        if cmd[0] == "9":
            ram[int(register[int(cmd[2])])] = register[int(cmd[1])]
        if cmd[0] == "0" and cmd[2] != "0":
            pos = int(register[int(cmd[1])])


main()
