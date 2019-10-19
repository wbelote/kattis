import sys


def main():
    line = sys.stdin.readline().split()
    log = []
    while len(line) > 1:
        log.append(line)
        line = sys.stdin.readline().split()

    solved = set()
    for i in range(len(log)):
        if log[i][2] == "right":
            solved.add(log[i][1])

    time = 0
    done = {x: False for x in solved}
    for i in range(len(log)):
        if log[i][1] in solved and not done[log[i][1]]:
            if log[i][2] == "right":
                time += int(log[i][0])
                done[log[i][1]] = True
            else:
                time += 20

    print(len(solved), time)


main()
