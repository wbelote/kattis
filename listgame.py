# Gives wrong answer on test 4. I have no idea why.

import math
import sys


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def factors(x):
    if is_prime(x):
        return []
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            if is_prime(x // i):
                return [i, x // i]
            return [i] + factors(x // i)


print(len(factors(int(sys.stdin.readline()))))
