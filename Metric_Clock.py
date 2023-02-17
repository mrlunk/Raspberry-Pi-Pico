# project in development... Not ready.

# Decimal Clock basics. (10 hour clock)
# https://en.wikipedia.org/wiki/Decimal_time

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
