import random

files = [[x] for x in "abcdefghij"]

levels = [[], []]
for i in range(10):
    lv = random.randrange(len(levels))
    levels[lv].append(i)
    if levels[-1]:
        levels.append([])
print(levels)

prev = []
for j in range(1, len(levels) - 1):
    for f in levels[j]:
        copy = levels[j - 1][:]
        parent = random.randrange(len(copy))
        files[f].append(files[copy.pop(parent)][0])

        copy += prev
        random.shuffle(copy)
        for i in range(len(copy)):
            if random.random() < 0.5:
                break
            files[f].append(files[copy.pop()][0])

    prev += levels[j - 1]

print(files)
print()

random.shuffle(files)
for f in files:
    print(f"{f[0]}:", end="")
    for val in f[1:]:
        print(f" {val}", end="")
    print()

# out = "10\n"
# for f in files:
#     out = f"{out}{f}:"
#     copy = files[:]
#     copy.remove(f)
#     random.shuffle(copy)
#     for i in range(9):
#         if random.random() < 0.5:
#             break
#         out = f"{out} {copy.pop()}"
#     out += "\n"
#
# print(out + random.choice(files) + "\n")
