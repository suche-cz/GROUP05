import datetime as dt

print(dt.date.today())
print(dt.datetime.now())

konec = dt.datetime(2024, 9, 4, 22, 0, 0)

print(konec - dt.datetime.now())
