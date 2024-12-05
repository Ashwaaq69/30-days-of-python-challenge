# Python datetime
# Python has got datetime module to handle date and time.

# import datetime

# print(dir(datetime))

from datetime import datetime

# now = datetime.now()
# # print(now)

# day = now.day                   
# month = now.month              
# year = now.year                 
# hour = now.hour                 
# minute = now.minute             
# second = now.second

# timeStamp = now.timestamp()
# print(day, month, hour, minute)
# print('timestamp', timeStamp)
# print(f'{day}/{month}/{year}, {hour}:{minute}')

# note:Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC.


# Formatting Date Output Using strftime

# new_year = datetime(2024, 1, 1)
# print(new_year)

# day = new_year.day
# month = new_year.month
# year = new_year.year
# hour = new_year.hour
# minute = new_year.minute
# second = new_year.second
# print(day, month, year, hour, minute) 
# print(f'{day}/{month}/{year}, {hour}:{minute}')


# Formatting date time using strftime method and the documentation can be found here.

# current date and time

# now = datetime.now()
# t = now.strftime("%H:%M:%S")
# print("time:", t)
# time_one = now.strftime("%m/%d/%Y, %H:%M:%S")

# print("time one:", time_one)
# time_two = now.strftime("%d/%m/%Y, %H:%M:%S")

# print("time two:", time_two)



# String to Time Using strptime

# date_string = "5 December, 2024"
# print("date_string =", date_string)
# date_object = datetime.strptime(date_string, "%d %B, %Y")
# print("date_object =", date_object)


# Using date from datetime

# from datetime import date
# d = date(2022, 1, 1)
# print(d)
# print('Current date:', d.today())    
# today = date.today()
# print("Current year:", today.year)   
# print("Current month:", today.month) 
# print("Current day:", today.day)    


# Time Objects to Represent Time

# from datetime import time

# a = time()
# print("a =", a)
# b = time(12, 5, 50)
# print("b =", b)
# c = time(hour=12, minute=49, second=50)
# print("c =", c)
# d = time(10, 30, 50, 200555)
# print("d =", d)


# Difference Between Two Points in Time Using

# from datetime import timedelta

# t1 = timedelta(weeks=12, days=10, hours=12, seconds=20)
# t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
# t3 = t1 - t2
# print('t1=',t1)
# print('t2=', t2)
# print("t3 =", t3)