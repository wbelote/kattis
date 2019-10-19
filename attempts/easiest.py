import sys

def sod(x):
    return sum([int(d) for d in str(x)])
    
def min_sod(x):
    x_sod = sod(x)
    guess = 10
    while True:
        guess += 1
        if sod(guess*x) == x_sod:
            return guess

def main():
    while True:
        x = int(sys.stdin.readline())
        if x == 0:
            return
        print(min_sod(x))

# main()
