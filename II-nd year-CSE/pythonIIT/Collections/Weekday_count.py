import datetime

count = 0

for i in range(1,32):
    d = datetime.date(2025,1,i)
    if d.weekday() == 6:
        count += 1

print(count)
