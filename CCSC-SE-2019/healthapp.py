import sys

data = " ".join(sys.stdin.readlines())
data = [float(d) for d in data.split()]

week = []
month = []
total = []
n_days = 0
n_weeks = 1
n_months = 1

for day in data:
    if day < -2.5:
        avg = "%0.2f" % (sum(total) / len(total))
        print(f"\nYear to Date for {n_days} days = {avg} mi.")
        break
    elif day < -1.5:
        avg = "%0.2f" % (sum(month) / len(month))
        print(f"\nMonth #{n_months} = {avg} mi.\n")
        n_months += 1
        month = []
        continue
    elif day < -0.5:
        avg = "%0.2f" % (sum(week) / len(week))
        print(f"Week #{n_weeks} = {avg} mi.")
        n_weeks += 1
        week = []
        continue

    week += [day]
    month += [day]
    total += [day]
    n_days += 1
