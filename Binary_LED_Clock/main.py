"""
Rough basic but working code. UNDER DEV.

Script by MrLunk 2023
https://github.com/mrlunk
"""

import machine
import network
import time
import ntptime
import utime

ledPinsSec = [2, 3, 4, 5, 6, 7]
ledPinsMin = [8, 9, 10, 11, 12, 13]
ledPinsHr = [14, 15, 16, 17, 18, 19]

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
    time.sleep(5)
    wlan = network.WLAN(network.STA_IF)
    Status = wlan.active()
    print (Status)
    ntptime.settime()
    wlan.deinit()

nBitsSec = len(ledPinsSec)
nBitsMin = len(ledPinsMin)
nBitsHr = len(ledPinsHr)

for i in range(nBitsSec):
    pin = machine.Pin(ledPinsSec[i], machine.Pin.OUT)

for i in range(nBitsMin):
    pin = machine.Pin(ledPinsMin[i], machine.Pin.OUT)

for i in range(nBitsHr):
    pin = machine.Pin(ledPinsHr[i], machine.Pin.OUT)

#-----------------------------------------------------------

def dispBinarySec(nSec):
    global ledPinsSec, nBitsSec
    for i in range(nBitsSec):
        machine.Pin(ledPinsSec[i], machine.Pin.OUT).value(nSec & 1)
        nSec >>= 1

def dispBinaryMin(nMin):
    global ledPinsMin, nBitsMin
    for i in range(nBitsMin):
        machine.Pin(ledPinsMin[i], machine.Pin.OUT).value(nMin & 1)
        nMin >>= 1

def dispBinaryHr(nHr):
    global ledPinsHr, nBitsHr
    for i in range(nBitsHr):
        machine.Pin(ledPinsHr[i], machine.Pin.OUT).value(nHr & 1)
        nHr >>= 1
        
connect_wifi()
Wifi_time_sync()

while True:
    countH = time.localtime()[3]+1
    countM = time.localtime()[4]
    countS = time.localtime()[5]
    
    dispBinarySec(countS)
    dispBinaryMin(countM)
    dispBinaryHr(countH)
    
    #---debug print time segments to console----------
    #print(countH,countM,countS)
    
    utime.sleep(1)
