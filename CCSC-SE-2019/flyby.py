import sys
import math

cases = int(sys.stdin.readline())
for case in range(cases):
    a, b, f, x0, y0, vx, vy = [float(x) for x in sys.stdin.readline().split()]
    d = min(map(lambda t: math.sqrt(
        ((x0 + vx * t) - (a * math.cos(f * t))) ** 2 +
        ((y0 + vy * t) - (a * math.sin(f * t))) ** 2
    ), range(11)))

    print("%0.5f" % d)
