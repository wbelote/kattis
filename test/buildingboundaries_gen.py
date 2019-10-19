import random

for line in range(10):
    nums = [str(random.randint(1, 20)) for _ in range(6)]
    print(" ".join(nums))
