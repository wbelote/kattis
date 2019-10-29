import sys


def main():
    correct = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    answers = [sys.stdin.readline().strip() for _ in range(n)]
    scores = [sum([a[i] == correct[i] for i in range(25)]) for a in answers]
    scores.sort()

    by_q = [sum([answers[j][i] == correct[i] for j in range(n)]) for i in range(25)]

    print(f"High Score = {max(scores) * 4}%")
    print(f"Median Score = {(scores[n // 2] + scores[(n - 1) // 2]) * 2.0}%")
    print(f"Question Number Answered Most Correctly = {1 + by_q.index(max(by_q))}")
    print(f"Question Number Answered Most Incorrectly = {1 + by_q.index(min(by_q))}")


main()
