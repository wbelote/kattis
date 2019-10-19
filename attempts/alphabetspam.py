import sys

symbols = "!\"#$%&'()*+,-./0123456789:;<=>?@[\\]^`{|}~"

line = sys.stdin.readline().strip()
print(line.count("_") / len(line))
print(sum([int(c.islower()) for c in line]) / len(line))
print(sum([int(c.isupper()) for c in line]) / len(line))
print(sum([int(c in symbols) for c in line]) / len(line))
