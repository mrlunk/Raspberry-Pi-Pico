"""
Rough basic but working code.
To be added:
- NTP stimesync evvery 24 hours
- Daylight savings time adjustment
- Reset button
- 12 / 24 hour clock switchable
- LED mode 'breathing' transitions (pulsating)
- LED mode Steady light bright/medium/low
- auto adjust brightness day/night (lightsensor ?)
- etc...

Script by MrLunk 2023
https://github.com/mrlunk
"""

import machine
import utime

ledPinsSec = [2, 3, 4, 5, 6, 7]
ledPinsMin = [8, 9, 10, 11, 12, 13]
ledPinsHr = [14, 15, 16, 17, 18, 19]

countS = 0
countM = 13
countH = 23

nBitsSec = len(ledPinsSec)
nBitsMin = len(ledPinsMin)
nBitsHr = len(ledPinsHr)

for i in range(nBitsSec):
    pin = machine.Pin(ledPinsSec[i], machine.Pin.OUT)

for i in range(nBitsMin):
    pin = machine.Pin(ledPinsMin[i], machine.Pin.OUT)

for i in range(nBitsHr):
    pin = machine.Pin(ledPinsHr[i], machine.Pin.OUT)

def loop():
    global countS, countM, countH
    countS = (countS + 1) % 60
    if countS == 0:
        countM = (countM + 1) % 60
        if countM == 0:
            countH = (countH + 1) % 24
    
    dispBinarySec(countS)
    dispBinaryMin(countM)
    dispBinaryHr(countH)
    
    utime.sleep(1)

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

while True:
    loop()


