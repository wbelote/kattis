import sys


def main():
    lo = 1
    hi = 1001
    response = ""
    while response != "correct":
        guess = (lo + hi) // 2
        sys.stdout.write(str(guess) + "\n")
        response = sys.stdin.readline().rstrip()
        if response == "lower":
            hi = guess
        elif response == "higher":
            lo = guess


if __name__ == '__main__':
    main()
