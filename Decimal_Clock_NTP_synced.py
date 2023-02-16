# project in development... Not ready.

# Decimal Clock basics. (10 hour clock)
# https://en.wikipedia.org/wiki/Decimal_time

import utime
import time

Dec_sec = 0
Dec_min = 0
Dec_hour = 0

while True:
    Dec_sec += 1
    
    if Dec_sec > 99:
        Dec_sec = 0
        Dec_min += 1
    
    if Dec_min > 99:
        Dec_min= 0
        Dec_hour += 1
        
    if Dec_hour > 9:
        Dec_hour =0
    
    
    utime.sleep_ms(864)
    print(Dec_hour,":",Dec_min,":",Dec_sec)
    print(time.localtime())

# 1 day has 10 decimal Hours
# 1 Decimal Hour Has 100 decimal minutes
# 1 Decimal clock minute has 100 decimal clock seconds
    
