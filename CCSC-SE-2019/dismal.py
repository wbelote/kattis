import sys


def dis_mult(nums):
    short = nums[0]
    long = nums[1]
    if len(short) > len(long):
        short = nums[1]
        long = nums[0]
    results = []
    for i in range(len(short))[::-1]:
        tempstr = ""
        for j in range(len(long)):
            if short[i] < long[j]:
                tempstr += short[i]
            else:
                tempstr += long[i]
        tempstr + ("0" * (len(long) - (i + 1)))
        results.append(tempstr)

    mySum = ""
    for item in results:
        mySum = dis_add((mySum, item))
    return mySum


def dis_add(nums):
    print(nums)
    short = nums[0]
    long = nums[1]
    if len(short) > len(long):
        short = nums[1]
        long = nums[0]
    mySum = long[:(len(long) - len(short))]
    for i in range(len(long) - len(mySum)):
        if long[len(mySum)] > short[i]:
            mySum += long[len(mySum)]
        else:
            mySum += short[i]
    print(f"{mySum}")
    return mySum


def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        ops = sys.stdin.readline().split()
        results = []
        for j in range(len(ops)):
            if "*" in ops[j]:
                results.append(int(dis_mult(ops[j].split("*"))))
            else:
                results.append(int(dis_add(ops[j].split("+"))))
        comp = ""
        if results[0] == results[1]:
            comp = " = "
        elif results[0] > results[1]:
            comp = " > "
        else:
            comp = " < "
    print("%d%s%d" % (results[0], comp, results[1]))


main()
