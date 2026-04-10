from collections import defaultdict
from datetime import datetime

dates = ["2026-03-10","2026-03-11","2026-03-12"]

d = defaultdict(list)

for i in dates:
    day = datetime.strptime(i,"%Y-%m-%d").strftime("%A")
    d[day].append(i)

print(d)
