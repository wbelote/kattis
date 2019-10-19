import sys

class Plot:
    def __init__(self, a, b):
        if a <= b:
            self.short = a
            self.long = b
        else:
            self.long = a
            self.short = b

    def area(self):
        return self.short * self.long

    def __str__(self):
        return f"{self.short}, {self.long}"

def reduce(plots):
    if len(plots) == 1:
        return plots[0]
    
    largest = plots[0]
    for i in range(1, len(plots)):
        plot = plots[i]
        if plot.long > largest.long:
            largest = plot
    plots.remove(largest)

    remaining = reduce(plots)
    return join(remaining, largest)

def join(a, b):
    albs = max(a.long, b.short) * a.short+b.long
    albl = max(a.long, b.long) * a.short + b.short
    asbl = max(a.short, b.short) * a.long + b.long
    asbs = max(a.short, b.long) * a.long + b.short
    mini = min(albs, albl, asbl, asbs)


    print(albs, albl, asbl, asbs)
    if mini == albs:
        return Plot(max(a.long, b.short), a.short+b.long)
    if mini == albl:
        return Plot(max(a.long, b.long), a.short + b.short)
    if mini == asbs:
        return Plot(max(a.short, b.short), a.long + b.long)
    if mini == asbl:
        return Plot(max(a.short, b.long), a.long + b.short)

num = int(sys.stdin.readline())
for i in range(num):
    plots = []
    dims = [int(n) for n in sys.stdin.readline().split()]
    for i in range(0,len(dims),2):
        plots.append(Plot(dims[i], dims[i+1]))

    print(str(reduce(plots).area()))
