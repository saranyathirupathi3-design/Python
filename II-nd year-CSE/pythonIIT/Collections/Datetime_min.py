from datetime import datetime

dates = ["2023-01-01","2022-05-10","2024-03-15"]

print(min(datetime.strptime(i,"%Y-%m-%d") for i in dates))
