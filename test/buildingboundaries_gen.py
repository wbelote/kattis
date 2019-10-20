import random

for line in range(100):
    nums = [str(random.randint(1, 50)) for _ in range(6)]
    print(" ".join(nums))
