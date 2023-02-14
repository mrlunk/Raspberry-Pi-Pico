# 24h Clock that Syncs with Network time server (NTP) every day at midnight (00:00:00) 
# The Clock automatically adjusts for Daylight Savings Time (DST) (AMS GMT).
# A Raspberry Pi Pico script written in Micro Python by: MrLunk 

# 24h Clock that Syncs with Network time server (NTP) every day at midnight (00:00:00) 
# The Clock automatically adjusts for Daylight Savings Time (DST) (AMS GMT).
# A Raspberry Pi Pico script written in Micro Python by: MrLunk 

import network
import time
import struct
import ntptime
from machine import Pin

led = Pin("LED", Pin.OUT)

Hour = ""
Minute = ""
Seconds = ""
Maanden = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Okt","Nov","Dec"]
WeekDagen = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

ssid = 'LunkTech3'
password = 'DoeMijDieMaar'

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(1)

    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        print('connected')
        status = wlan.ifconfig()
        print( 'ip = ' + status[0] )
        print("___Time synced with NTP server______")
        
def Wifi_time_sync():
    wlan = network.WLAN(network.STA_IF)
    Status = wlan.active()
    ntptime.settime()

def last_sunday_of_month(year, month):
    t = time.mktime((year, month, 31, 0, 0, 0, 0, 0, 0))
    wday = time.localtime(t)[6]
    t = t - (wday + 1) * 24 * 60 * 60
    date = time.localtime(t)[:3]
    return date

def Connect_and_sync():
    wlan = network.WLAN(network.STA_IF)
    connect_wifi()
    Wifi_time_sync()
    wlan.deinit()
    
#--------------------------------------------------------------------------------

Connect_and_sync()

while True:
    year = time.localtime()[0]
    DST_start_date = last_sunday_of_month(year, 3)
    DST_end_date = last_sunday_of_month(year, 10)
    
    current_date = time.localtime()[:3]
    
    DST_Adjustment = 1 if DST_start_date < current_date < DST_end_date else 0
    current_time = time.localtime()
    current_time_list = list(current_time)
    current_time_list[3] -= DST_Adjustment
    if current_time_list[3] == -1:
        current_time_list[3] == 23
    final_time = tuple(current_time_list)
    
    Year = final_time[0]
    Maand = final_time[1]-1
    Day = final_time[2]
    Hour = final_time[3]+1
    Minute = final_time[4]
    Second = final_time[5]
    DayOTWeek = final_time[6]
    DayNumber = final_time[7]
    
    print("Time: ",Hour,":",Minute,":",Second)
    print(WeekDagen[DayOTWeek],Maanden[Maand],Day,Year)
    print("Day of the year: ",DayNumber) 
    print("")
    time.sleep(1)

    if Hour == 0:
        if Minute == 0:
            if Second == 0:
                print("Before Sync: ",(final_time))
                Connect_and_sync()
                print("After Sync: ",(final_time))
                print("")



