"""
This code converts regular time (in hours, minutes, and seconds) to metric time 
(in metric hours, metric minutes, and metric seconds). Metric time uses a base 10
system instead of the base 60 system used in regular time.

The code first gets the number of seconds past midnight using the utime.time() 
function. It then calculates the decimal hours by dividing the number of seconds 
by 3600 (the number of seconds in an hour). It then converts decimal hours to metric 
time by multiplying by 100000 and dividing by 24. This gives us the number of metric 
seconds since midnight.

The metric time is then broken down into metric hours, metric minutes, and metric 
seconds using integer division and modulus operations.

The code then prints out both the metric time and regular time using the print() 
function. It also includes a 96ms delay using the utime.sleep_ms() function to 
make sure the code doesn't execute too quickly.

Metric Time information: https://en.wikipedia.org/wiki/Metric_time

Metric time clock example: https://minkukel.com/en/clocks/metric-clock/ (not mine)
"""

# Micropython Script for Raspberry Pi Pico by: MrLunk

import utime
import time


while True:
    # Get seconds past midnight
    seconds_past_midnight = utime.time() % 86400

    # Convert seconds to decimal hours
    decimal_hours = seconds_past_midnight / 3600

    # Convert decimal hours to Metric time
    metric_time = decimal_hours / 24 * 100000

    # Extract the hours, minutes, and seconds components of Metric time
    metric_seconds = int(metric_time % 100)
    metric_minutes = int((metric_time // 100) % 100)
    metric_hours = int(metric_time // 10000)

    # Print the Metric time in HH:MM:SS format
    print("Metric time: ","{:02d}:{:02d}:{:02d}".format(metric_hours, metric_minutes, metric_seconds))
    # Print the Regular time in HH:MM:SS format
    print("Regular Time:","{:02d}:{:02d}:{:02d}".format((time.localtime()[3]),(time.localtime()[4]),(time.localtime()[5])))
    utime.sleep_ms(96)
    print("______________________")
