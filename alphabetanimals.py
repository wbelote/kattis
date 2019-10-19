import sys

def main():
    last = sys.stdin.readline().rstrip()[-1]
    n = int(sys.stdin.readline())
    pos_answers = []
    pos_answers_set = set()
    first_letters = {a:0 for a in "abcdefghijklmnopqrstuvwxyz"}
    last_letters = {a:0 for a in "abcdefghijklmnopqrstuvwxyz"}

    for i in range(n):
        line = sys.stdin.readline().rstrip()
        if line[0] == last:
            firstlast = (line[0], line[-1])
            if firstlast not in pos_answers_set:
                pos_answers.append(line)
                pos_answers_set.add(firstlast)
            last_letters[line[-1]] += 1

        first_letters[line[0]] += 1

    if not pos_answers:
        return "?"
    for ans in pos_answers:
        if first_letters[ans[-1]] <= (ans[0] == ans[-1]):
            return ans + "!"

    return pos_answers[0]
        
            
print(main())
