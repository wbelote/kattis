import sys

register = ['000'] * 10
ram = sys.stdin.split("\n")
ram += ['000'] * (1000 - len(ram))
global steps
steps = 0
pos = 0


def goto(cmd):
    line = ram[pos]
    global steps
    if cmd == '1':
        print(steps + 1)
        return
    elif line[0] == '2':
        register[int(line[1])] = int(line[2])
        steps += 1
    elif line[0] == '3':
        pass


