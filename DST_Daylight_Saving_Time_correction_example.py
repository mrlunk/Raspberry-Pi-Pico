# https://en.wikipedia.org/wiki/Daylight_saving_time
# Script in MicroPython for Raspberry pi Pico
# Daylight savings correction example By: MrLunk

import time

def last_sunday_of_month(year, month):
    t = time.mktime((year, month, 31, 0, 0, 0, 0, 0, 0))
    wday = time.localtime(t)[6]
    t = t - (wday + 1) * 24 * 60 * 60
    date = time.localtime(t)[:3]
    return date

year = time.localtime()[0]
DST_start_date = last_sunday_of_month(year, 3)
DST_end_date = last_sunday_of_month(year, 10)

current_date = time.localtime()[:3]
DST_Adjustment = 1 if DST_start_date < current_date < DST_end_date else 0

current_time = time.localtime()
current_time_list = list(current_time)
current_time_list[3] -= DST_Adjustment
final_time = tuple(current_time_list)

print(final_time)
