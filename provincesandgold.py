import sys


def main():
    line = sys.stdin.readline().split()
    total = sum([int(line[i]) * (3 - i) for i in range(3)])

    victory = ['Estate', 'Duchy', 'Province']
    treasure = ['Copper', 'Silver', 'Gold']
    if total < 2:
        print("Copper")
    elif total >= 8:
        print("Province or Gold")
    else:
        print(
            victory[(total - 2) // 3],
            "or",
            treasure[total // 3],
        )


main()
