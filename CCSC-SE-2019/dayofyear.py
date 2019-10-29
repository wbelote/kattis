import sys

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

cases = int(sys.stdin.readline().strip())

for case in range(cases):
    m, d, y = [int(n) for n in sys.stdin.readline().strip().split('/')]

    doy = sum(months[:m-1]) + d
    if m > 2:
        if y % 4 == 0 and (not y % 100 == 0 or y % 400 == 0):
            doy += 1

    if m < 3:
        m += 12
        y -= 1
    j = y // 100
    k = y % 100
    h = int((d + 26 * (m + 1) // 10 + k + k // 4 + j // 4 + 5 * j) % 7)
    if m > 12:
        m -= 12
        y += 1

    if doy % 10 == 1:
        suffix = 'st'
    elif doy % 10 == 2:
        suffix = 'nd'
    elif doy % 10 == 3:
        suffix = 'rd'
    else:
        suffix = 'th'

    print(f'{m}/{d}/{y} is a {days[h]} and the {doy}{suffix} day of the year.')