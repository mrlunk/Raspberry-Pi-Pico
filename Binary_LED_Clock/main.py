import machine
import network
import time
import ntptime
import utime

# WiFi credentials
ssid = 'LunkTech3'
password = 'DoeMijDieMaar'

# LED pins for seconds, minutes and hours
ledPinsSec = [0, 1, 2, 3, 4, 5]
ledPinsMin = [6, 7, 8, 9, 10, 11]
ledPinsHr = [12, 13, 14, 15, 16, 17]

# Number of bits for each LED group
nBitsSec = len(ledPinsSec)
nBitsMin = len(ledPinsMin)
nBitsHr = len(ledPinsHr)

# Initialize all LED pins
for pin in ledPinsSec + ledPinsMin + ledPinsHr:
    machine.Pin(pin, machine.Pin.OUT).low()

# Connect to WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    max_wait = 10
    while max_wait > 0 and wlan.status() not in [network.STAT_GOT_IP, network.STAT_CONNECTING]:
        print('waiting for connection...')
        time.sleep(1)
        max_wait -= 1

    if wlan.status() != network.STAT_GOT_IP:
        raise RuntimeError('network connection failed')
    else:
        print('connected')
        print('ip =', wlan.ifconfig()[0])

# Synchronize time with NTP server
def Wifi_time_sync():
    ntptime.settime()
    network.WLAN(network.STA_IF).deinit()

# Display binary value on the seconds LEDs
def dispBinarySec(nSec):
    for i in range(nBitsSec):
        machine.Pin(ledPinsSec[i], machine.Pin.OUT).value(nSec & 1)
        nSec >>= 1

# Display binary value on the minutes LEDs
def dispBinaryMin(nMin):
    for i in range(nBitsMin):
        machine.Pin(ledPinsMin[i], machine.Pin.OUT).value(nMin & 1)
        nMin >>= 1

# Display binary value on the hours LEDs
def dispBinaryHr(nHr):
    for i in range(nBitsHr):
        machine.Pin(ledPinsHr[i], machine.Pin.OUT).value(nHr & 1)
        nHr >>= 1

# Main loop
connect_wifi()
Wifi_time_sync()

while True:
    countH, countM, countS, *_ = time.localtime()  # Get current time

    # Display current time on LEDs
    dispBinarySec(countS)
    dispBinaryMin(countM)
    dispBinaryHr(countH+1)  # DST correction will be added later

    # Repeat NTP time synchronization every day at midnight
    if countH == 0 and countM == 0 and countS == 0:
        connect_wifi()
        Wifi_time_sync()

    # Debug print time segments to console
    print(countH, countM, countS)

    utime.sleep(1)  # Wait for 1 second
