out = []

def factors(x):
    for d in x:
        if int(x) % int(d):
            return False
    return True

for i in range(9*8*7*6*5*4):
    print(i, end=" ")
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    big = i
    line = ""
    for j in range(6):
        n = int(big % (9 - j))
        big /= 9 - j
        print(n, end="")
        line += str(digits.pop(n))
    if factors(line):
        out.append(line)
    print()

print()
out.sort()
print(out)

print(len(out), len(set(out)))
