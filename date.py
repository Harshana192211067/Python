import datetime
d=12
year=1984
m=3
days=datetime.date(year,m,d)
day=days.strftime("%A")
print(day)
