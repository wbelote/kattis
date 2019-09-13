import math
import sys


def angle2(mid, p1, p2):
    a1 = math.atan2(p1[1] - mid[1], p1[0] - mid[0])
    a2 = math.atan2(p2[1] - mid[1], p2[0] - mid[0])
    return angle_diff(a1, a2)


def angle_diff(a1, a2):
    return min([abs(a1 - a2), 2 * math.pi - abs(a1 - a2)])


def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        line = sys.stdin.readline().split()
        k = int(line[0])
        a, b, c = [(float(line[i]), float(line[i + 1])) for i in (1, 3, 5)]
        unzip = [[x for x, y in (a, b, c)], [y for x, y in (a, b, c)]]
        min_x, max_x, min_y, max_y = min(unzip[0]), max(unzip[0]), min(unzip[1]), max(unzip[1])

        # Use the mean of the corner points to make initial guess,
        # calculate relevant angles and their mean
        point = [sum(val) / 3 for val in unzip]
        angles = [angle2(a, point, b), angle2(b, point, c), angle2(c, point, a)]
        mean = sum(angles) / 3
        coef = 1

        while max(angles) - min(angles) > 0.000001:
            # Update the guess point based on the errors
            # For each point, move the guess perpendicular to the line between that point and the guess
            # by an amount proportional to how far that angle is from the mean angle.

            # dirs: direction to move the guess for each point
            # errs: difference between each angle and the mean angle
            # diff: change in the guess
            dirs = [[point[1] - x[1], x[0] - point[0]] for x in (a, b, c)]
            errs = [(angle - mean) * abs(angle - mean) for angle in angles]
            x_diff = [dirs[i][0] * errs[i] for i in range(3)]
            y_diff = [dirs[i][1] * errs[i] for i in range(3)]

            # print()
            # print("point", point)
            # print("angles", angles, mean)
            # print("errs", errs)
            # print("dirs", dirs)
            # print("x diff", x_diff, sum(x_diff))
            # print("y diff", y_diff, sum(y_diff))

            point[0] += sum(x_diff) * 2 ** coef
            point[1] += sum(y_diff) * 2 ** coef
            angles = [angle2(a, point, b), angle2(b, point, c), angle2(c, point, a)]
            mean = sum(angles) / 3

            if not (min_x <= point[0] <= max_x and min_y <= point[1] <= max_y):
                coef -= 1
                point = [sum(val) / 3 for val in unzip]
                angles = [angle2(a, point, b), angle2(b, point, c), angle2(c, point, a)]
                mean = sum(angles) / 3

        print(k, point[0], point[1])


main()
