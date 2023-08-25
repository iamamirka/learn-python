# In Python, we use the datetime module using an import
from datetime import datetime, date

# Get the current year, month, day
today = date.today()
print(today)

# Get the current year, month, day, hour, minute, second, ms
now = datetime.now()
print(now)

today1 = datetime.today()
print(today1)

# Use the datime constructor
someday = datetime(year=2022, month=9, day=21, hour=18)
print(someday)

print(type(someday))

span = someday - now
print(span)
print(type(span))