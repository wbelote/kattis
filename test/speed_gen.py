import random

out = "1000 1000000\n"
for i in range(1000):
    # d = random.randint(0, 1000)
    # s = random.randint(-1000, 1000)
    # total_time += d / (s + c)
    out += "1 -1000\n"
#
# out = out.replace("TIME", str(total_time))
with open("speed_test.txt", "w") as f:
    f.write(out)
