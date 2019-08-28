import random

output = "1000000 100000"
for i in range(100000):
    if i < 50000:  # random.random() < 0.5:
        output += f"\nF {random.randint(1, 99999)}"
    else:
        first = random.randint(2, 99998)
        second = random.randint(2, 99998)
        while first == second:
            first = random.randint(2, 99998)
            second = random.randint(2, 99998)
        output += f"\nC {min(first, second)} {max(first, second)}"

with open("supercomputer-input.txt", "w") as f:
    f.write(output)
