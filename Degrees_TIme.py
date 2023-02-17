"""
This is a Python script that calculates the number of degrees that the Earth has turned since midnight, and continuously prints the result along with the current timestamp.

The script first sets the number of seconds per day and per degree, and then enters an infinite loop. Within the loop, it uses the time module to get the current time as a timestamp, calculates the number of seconds that have elapsed since midnight, and then converts that to the number of degrees that the Earth has turned by dividing by the number of seconds per degree.

It then prints out the result along with the current timestamp using the print function, and then waits for one second using the time.sleep function before starting the loop again.
"""

# A Micro Python Script for Raspberry Pi Pico by: MrLunk

import time

SECONDS_PER_DAY = 86400
SECONDS_PER_DEGREE = SECONDS_PER_DAY / 360

while True:
    current_time = time.time()
    seconds_since_midnight = current_time % SECONDS_PER_DAY
    degrees_turned = seconds_since_midnight / SECONDS_PER_DEGREE

    print("At timestamp:","{:02d}:{:02d}:{:02d}".format((time.localtime()[3]),(time.localtime()[4]),(time.localtime()[5])))
    print("The earth has turned", degrees_turned, "degrees since midnight.")
    time.sleep(1)
    print("_____________________________________________________________")
