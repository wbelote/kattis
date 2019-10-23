import sys


class Runner:
    def __init__(self, name, first, other):
        self.name = name
        self.first = float(first)
        self.other = float(other)
        self.diff = self.first - self.other

    def __str__(self):
        return self.name


class Relay:
    def __init__(self, members):
        self.members = members
        self.total = sum(m.first for m in members)
        self.order()

    def order(self):
        for i in range(1, 4):
            if self.members[i].diff < self.members[0].diff:
                self.members[0], self.members[i] = self.members[i], self.members[0]
        self.total = self.members[0].first + self.members[1].other + self.members[2].other + self.members[3].other

    def insert(self, new):
        if new in self.members:
            return

        options = []
        for i in range(4):
            copy = self.members[:]
            copy[i] = new
            options += [Relay(copy)]

        for o in options:
            if o.total < self.total:
                self.members = o.members
                self.total = o.total

    def __str__(self):
        return f"{self.total}\n" + "\n".join([str(m) for m in self.members])


def main():
    n = int(sys.stdin.readline())
    runners = []
    for i in range(n):
        name, first, other = sys.stdin.readline().split()
        runners += [Runner(name, first, other)]

    runners.sort(key=lambda a: a.other)
    relay = Relay(runners[:4])
    runners = runners[4:]
    if runners:
        runners.sort(key=lambda a: a.first)
        relay.insert(runners[0])
    print(relay)


if __name__ == '__main__':
    main()
