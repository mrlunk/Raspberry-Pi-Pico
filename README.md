# Raspberry Pi Pico
 Some Pi pico MicroPython scripts...
 
## DateLastSundayInMarch.py

This is a Python script that calculates the date of the last Sunday of March in a given year. The function last_sunday_of_march takes a year as an argument and returns a tuple of (year, month, day) for the date of the last Sunday of March.

The script first creates a timestamp t for March 31st of the given year using the mktime function from the time module. Then, it uses the localtime function to extract the day of the week (Sunday is represented by 6) from the timestamp. The script then subtracts the number of seconds corresponding to the number of days from March 31st to the last Sunday of March, and calculates the date using the localtime function again.

Finally, the script prints the date of the last Sunday of March in the year obtained from the current local time using the strftime function.

## Wifi_NTP_TimeSynced_Clock.py 

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

By: MrLunk 2023
