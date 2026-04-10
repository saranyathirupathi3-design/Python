import datetime

d = datetime.datetime.strptime("2026-03-10", "%Y-%m-%d")
print(d.strftime("%U"))
