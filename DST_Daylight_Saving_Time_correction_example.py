# https://en.wikipedia.org/wiki/Daylight_saving_time
# Script in MicroPython for Raspberry pi Pico
# Daylight savings correction example By: MrLunk

import time

# Define a function to calculate the last Sunday of a given month and year
def last_sunday_of_month(year, month):
    # Calculate the timestamp for the 31st of the given month and year
    t = time.mktime((year, month, 31, 0, 0, 0, 0, 0, 0))
    # Get the weekday of the 31st
    wday = time.localtime(t)[6]
    # Subtract the weekday from the 31st to get the timestamp for the last Sunday of the month
    t = t - (wday + 1) * 24 * 60 * 60
    # Get the date of the last Sunday of the month
    date = time.localtime(t)[:3]
    return date

# Get the current year
year = time.localtime()[0]

# Calculate the last Sunday of March and October for the current year
DST_start_date = last_sunday_of_month(year, 3)
DST_end_date = last_sunday_of_month(year, 10)

# Get the current date
current_date = time.localtime()[:3]

# Calculate the DST adjustment (1 hour if within DST, 0 hours if outside DST)
DST_Adjustment = 1 if DST_start_date < current_date < DST_end_date else 0

# Get the current time
current_time = time.localtime()

# Convert the current time to a list for modification
current_time_list = list(current_time)

# Subtract the DST adjustment from the current time
current_time_list[3] -= DST_Adjustment
if current_time_list[3] == -1:
    current_time_list[3] == 23

# Convert the modified time back to a tuple
final_time = tuple(current_time_list)

# Print the final corrected time
print(final_time)

