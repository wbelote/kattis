import random
import sys
import time
import math

start = time.time()


def dist(a, b):
    return round(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5)


n = int(sys.stdin.readline())
if n == 1:
    print(0)
    sys.exit(0)
stop = 1.95 - n / 200000
points = tuple(tuple(float(x) for x in sys.stdin.readline().split()) for i in range(n))
mid = (sum([x for x, y in points]) / n, sum([y for x, y in points]) / n)
tans = [[math.atan2(points[i][1]-mid[1], points[i][0]-mid[0]), i] for i in range(n)]
tans.sort()

path = [i for t, i in tans]
path_points = tuple(points[x] for x in path)
best_dist = sum([dist(path_points[i], path_points[i + 1]) for i in range(n - 1)])
best_path = tuple(path[:])

loops = 0
while True:
    loops += 1

    swap = [random.choice(range(n)) for i in range(2)]
    while swap[0] == swap[1]:
        swap = [random.choice(range(n)) for i in range(2)]
    swap.sort()
    path = list(best_path[:])
    path[min(swap)], path[max(swap)] = path[max(swap)], path[min(swap)]

    path_points = tuple(points[x] for x in path)
    path_dist = sum([dist(path_points[i], path_points[i + 1]) for i in range(n - 1)])
    if path_dist < best_dist:
        best_dist = path_dist
        best_path = tuple(path[:])

    if time.time() - start >= stop:
        for p in best_path:
            print(p)
        # print(time.time() - start)
        # print(loops)
        break
