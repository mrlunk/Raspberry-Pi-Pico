# https://en.wikipedia.org/wiki/Daylight_saving_time
# Script in MicroPython for Raspberry pi Pico
# Daylight savings correction example By: MrLunk

import time

DST_Adjustment = 0

def last_sunday_of_march(year):
    # Calculate the timestamp for March 31st of the current year
    t = time.mktime((year, 3, 31, 0, 0, 0, 0, 0, 0))
    # Use the localtime function to get the weekday of March 31st
    wday = time.localtime(t)[6]
    # Subtract the weekday from March 31st to get the timestamp for the last Sunday of March
    t = t - (wday + 1) * 24 * 60 * 60
    # Use the localtime function to get the date of the last Sunday of March
    date = time.localtime(t)[:3]
    return date

def last_sunday_of_oktober(year):
    t = time.mktime((year, 10, 31, 0, 0, 0, 0, 0, 0))
    wday = time.localtime(t)[6]
    t = t - (wday + 1) * 24 * 60 * 60
    date = time.localtime(t)[:3]
    return date

# ----------------------------------------------------------------------

# Get the current year
year = time.localtime()[0]
# Call the last_sunday_of_march function to get the date of the last Sunday of March of the current year
DST_start_date = last_sunday_of_march(year)
DST_end_date = last_sunday_of_oktober(year)

#--------------------- -------------------------------------------------
# Check if date is between DST_start_date and DST_end_date
# depending on the result substract an hour from the clock.

Current_Date = date = time.localtime()[:3]
# print("Current Date:",Current_Date)

if Current_Date > DST_start_date:
    if Current_Date < DST_end_date:
        DST_Adjustment = 1
        
if Current_Date < DST_start_date:
    DST_Adjustment = 0
    
if Current_Date > DST_end_date:
    DST_Adjustment = 0
    
print(DST_Adjustment)

#---------------------------------------------------------------------
# Time Tuple to list - subtract DST_Adjustment (1 or 0) from 4th value of tuple
# turn list back into tuple

Current_time = time.localtime()
Current_time = time.localtime()
Current_time_list=list(time.localtime())
Current_time_list[3]-=DST_Adjustment
Final_time = tuple(Current_time_list)

print(Final_time)


