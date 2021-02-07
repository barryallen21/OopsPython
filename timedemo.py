import datetime
import time
import calendar

print(time.localtime())
print(time.asctime(time.localtime()))
print(datetime.datetime.now())
print(datetime.date(2021,6,8))
print(datetime.datetime(21,6,8,12,35,10))
dt=datetime.date(21,6,8)
print(dt)
if(datetime.datetime.now().day<dt.day):
    print("yest")
else:
    print("tomorrow")

print(calendar.month(2021,6))
print(calendar.calendar(100))
print(calendar.day_name[0])
print(calendar.month_name[2])
print(calendar.prcal(2012))


#if calendar.day_name == 0:
 #   return sunday
