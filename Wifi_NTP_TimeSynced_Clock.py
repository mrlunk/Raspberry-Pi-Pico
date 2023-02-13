# Script by: Peter Lunk 

"""
This MicroPython script is for Raspberry Pi Pico W (Wifi) device
that connects to a Wi-Fi network and synchronizes its time with 
a NTP (Network Time Protocol) server. 
The script first sets up a connection to the Wi-Fi network using
the specified ssid (network name) and password, and then sets
the device's time using the ntptime.settime() function. 
The device continuously retrieves the current time from internal
clock and displays it along with the current date and day of the
year on the serial monitor every second.
The script synchronizes the time with NTP every day at midnight.
"""

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
    ntptime.settime()
    print("_____________________________________________")
    
#--------------------------------------------------------------------------------
connect_wifi()
Wifi_time_sync()

while True:
    Year = time.localtime()[0]
    Maand = (time.localtime()[1])-1
    Day = time.localtime()[2]
    Hour = time.localtime()[3]+1
    Minute = time.localtime()[4]
    Second = time.localtime()[5]
    DayOTWeek = (time.localtime()[6])
    DayNumber = time.localtime()[7]
    
    # Daylightsavings + or - hour auto adjustment.
    #if Maand == 
    
    # ---- Print Date time info to Serial Monitor -------------------------------------
    print("Time: ",Hour,":",Minute,":",Second)
    print(WeekDagen[DayOTWeek],Maanden[Maand],Day,Year)
    print("Day of the year: ",DayNumber) 
    print("")
    time.sleep(1)
    
    # ---- Sync with NTP time server once per Day at Midnight:
    if Hour == 11:
        if Minute == 8:
            if Second == 0:
                print("Before Sync: ",(time.localtime()))
                Wifi_time_sync()
                print("After Sync: ",(time.localtime()))
                print("")
