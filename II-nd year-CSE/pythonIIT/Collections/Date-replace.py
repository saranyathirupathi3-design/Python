import datetime

year = 2028
print(datetime.date(year, 1, 1).replace(year=year).year % 4 == 0)
