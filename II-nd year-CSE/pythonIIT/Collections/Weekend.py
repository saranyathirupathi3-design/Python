import datetime

d = datetime.date(2026,3,14)

print("Weekend" if d.weekday() >= 5 else "Weekday")
