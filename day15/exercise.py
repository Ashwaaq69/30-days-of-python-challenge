from datetime import datetime

# 1:Get the current day, month, year, hour, minute and timestamp from datetime module

# now = datetime.now()
# print(now)
# day = now.day
# month = now.month
# year = now.year
# hour = now.hour
# minute = now.minute
# timestamp = now.timestamp()
# print(f"Day: {day}")
# print(f"Month: {month}")
# print(f"Year: {year}")
# print(f"Hour: {hour}")
# print(f"Minute: {minute}")
# print(f"Timestamp: {timestamp}")


# 2:Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

# now = datetime.now()
# t = now.strftime("%m:%d:%y")
# print("date:", t)

# Today is 5 December, 2024. Change this time string to time.

# date_string = '5 december, 2024'
# print('date_string=' ,date_string )

#4: Calculate the time difference between now and new year.
from datetime import datetime

# Get the current date and time
# now = datetime.now()

# # Define the next New Year
# next_new_year = datetime(year=now.year + 1, month=1, day=1, hour=0, minute=0, second=0)

# # Calculate the difference
# time_difference = next_new_year - now

# # Extract days, hours, minutes, and seconds from the difference
# days = time_difference.days
# hours, remainder = divmod(time_difference.seconds, 3600)
# minutes, seconds = divmod(remainder, 60)

# # Print the results
# print(f"Time until New Year: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")


# 5:Calculate the time difference between 1 January 1970 and now.



# Define the start date (1 January 1970)
# start_date = datetime(1970, 1, 1)

# # Get the current date and time
# now = datetime.now()

# # Calculate the time difference
# time_difference = now - start_date

# # Extract days, hours, minutes, and seconds from the difference
# total_days = time_difference.days
# total_seconds = time_difference.total_seconds()
# hours, remainder = divmod(time_difference.seconds, 3600)
# minutes, seconds = divmod(remainder, 60)

# # Print the results
# print(f"Time since 1 January 1970:")
# print(f"Total days: {total_days}")
# print(f"Total seconds: {total_seconds}")
# print(f"Current time breakdown: {hours} hours, {minutes} minutes, {seconds} seconds.")


