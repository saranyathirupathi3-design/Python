import datetime

d = datetime.date(2026,3,10)

prev = d.replace(month=d.month-1)
print(prev)
