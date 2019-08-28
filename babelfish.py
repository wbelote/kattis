import sys

def main():
    entries = {}
    for line in sys.stdin:
        words = line.split()
        if len(words) >= 2:
            entries[words[1]] = words[0]
        if len(words) == 1:
            if words[0] in entries.keys():
                print(entries[words[0]])
            else:
                print("eh")

main()
