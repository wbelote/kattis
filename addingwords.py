import sys


def main():
    names = {}
    defined = set()
    while True:
        line = sys.stdin.readline().rstrip()
        command = line.split()
        if not command:
            return
        elif command[0] == "def":
            names[command[1]] = command[2]
            names[command[2]] = command[1]
            defined |= {command[1], command[2]}
        elif command[0] == "calc":
            in_line = command[1::2]
            if set(in_line) <= defined:
                new = line[4:-1]
                for val in in_line:
                    new = new.replace(f" {val} ", f" {names[val]} ")
                result = str(eval(new))
                if result in defined:
                    print(f"{line[5:]} {names[result]}")
                else:
                    print(f"{line[5:]} unknown")
            else:
                print(f"{line[5:]} unknown")
        else:
            names = {}
            defined = set()


if __name__ == '__main__':
    main()
