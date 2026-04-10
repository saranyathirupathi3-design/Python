from datetime import datetime, timedelta

activities = [
("A","2026-03-25 10:00"),
("B","2026-03-26 08:00"),
("C","2026-03-24 09:00")
]

now = datetime(2026,3,26,12,0)

for user, t in activities:
    time = datetime.strptime(t,"%Y-%m-%d %H:%M")
    if now - time <= timedelta(hours=24):
        print(user)
