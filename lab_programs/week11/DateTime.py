import datetime
now = datetime.datetime.now()
print("TIME:", now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print("Year:", year(now))
print("Month:", month(now))
print("Date:", day(now))
print("Time:", t(now))