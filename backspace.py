import sys

line = sys.stdin.readline().rstrip()
len_line = len(line)

out = [""] * len_line
end = 0
for i in range(len_line):
    char = line[i]
    if char == "<":
        end -= 1
        out[end] = ""
    else:
        out[end] = char
        end += 1

print("".join(out))
