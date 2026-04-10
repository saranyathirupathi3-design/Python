from collections import Counter

dates = ["2026-03-10","2026-03-10","2026-03-11"]

c = Counter(dates)

for i in c:
    if c[i] > 1:
        print(i)
