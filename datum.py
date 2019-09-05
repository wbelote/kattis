import sys

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]

line = sys.stdin.readline().split()
d, m = [int(x) - 1 for x in line]
day_number = d + sum(months[:m])
print(days[day_number % 7])