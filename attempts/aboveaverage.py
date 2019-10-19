import sys, math

def form(s):
	out = str(round(s*100000)/1000)
	if out[1] == ".":
		return out[:5] + "%"
	return out[:6] + "%"
	

def main():
    c = int(sys.stdin.readline())
    for i in range(c):
        line = sys.stdin.readline().split()
        n = int(line[0])
        grades = [int(x) for x in line[1:]]
        m = sum(grades)/len(grades)
        above = [g > m for g in grades]
        
        print(form(sum(above)/len(above)))

main()
