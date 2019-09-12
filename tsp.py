import sys, time, math, itertools

start = time.time()


def dist(a, b):
    return round(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5)


n = int(sys.stdin.readline())
if n == 1:
    print(0)
    sys.exit(0)
stop = 1.95 - n / 200000
points = tuple(tuple(float(x) for x in sys.stdin.readline().split()) for i in range(n))

best_dist = sum([dist(points[i], points[i - 1]) for i in range(n)])
best_path = tuple(range(n))

loops = 0
for path in itertools.permutations(range(n)):
    path_points = tuple(points[x] for x in path)
    path_dist = sum([dist(path_points[i], path_points[i + 1]) for i in range(n - 1)])
    if path_dist < best_dist:
        best_dist = path_dist
        best_path = path

    if time.time() - start >= stop:
        for p in best_path:
            print(p)
        # print(time.time() - start)
        break
