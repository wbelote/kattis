import sys

pronouns = "me you she her he him".split()
possessive = "my mine your yours hers his".split()


def split(sentence):
    words = [""]
    for l in sentence:
        if l.isalnum():
            words[-1] += l
        else:
            words.append(l)
            words.append("")
    return words


def main():
    n = int(sys.stdin.readline())
    for case in range(n):
        line = sys.stdin.readline().strip()
        words = split(line)
        for i in range(len(words)):
            if words[i].lower() in pronouns:
                words[i] = "Kanye"
            if words[i].lower() in possessive:
                words[i] = "Kanye's"
        print("".join(words))


main()
