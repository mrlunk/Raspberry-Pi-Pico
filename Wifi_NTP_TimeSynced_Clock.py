# WORK IN PROGRESS - Under Construction
# Script by: Peter Lunk 

import network
import socket
import time
import struct
import ntptime
from machine import Pin

led = Pin("LED", Pin.OUT)

x = 1
Hour = ""
Minute = ""
Seconds = ""
Maanden = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Okt","Nov","Dec"]
WeekDagen = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

TimeCheck = 300

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
        
def Wifi_time_sync():
    wlan = network.WLAN(network.STA_IF)
    Status = wlan.active()
    print (Status)
    print("_____________________________________________")
    
#--------------------------------------------------------------------------------
connect_wifi()
ntptime.settime()
Wifi_time_sync()

while True:
    Year = time.localtime()[0]
    Maand = (time.localtime()[1])-1
    Day = time.localtime()[2]
    Hour = time.localtime()[3]
    Minute = time.localtime()[4]
    Second = time.localtime()[5]
    DayOTWeek = (time.localtime()[6])
    DayNumber = time.localtime()[7]
    
    # ---- Print Date time info to Serial Monitor -------------------------------------
    print("Time: ",Hour,":",Minute,":",Second)
    print(WeekDagen[DayOTWeek],Maanden[Maand],Day,Year)
    print("Day of the year: ",DayNumber) 
    print("")
    time.sleep(1)
    
    # ---- Sync with NTP time server once per Day at Midnight:
    if Hour == 0:
        if Minute == 0:
            if Second == 0:
                print("")
                Wifi_time_sync()
                print("")
                print ("Time Synced at 00:00:00 ....")
                print("")

