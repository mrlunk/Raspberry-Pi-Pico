# Raspberry Pi Pico
 Some Pi pico scripts
 
## DateLastSundayInMarch.py

This code defines a function last_sunday_of_march that takes a
year as its input and returns the date of the last Sunday of 
March for that year.

The function first calculates the timestamp for March 31st of
the given year using the time.mktime function. Then, it uses
the time.localtime function to get the weekday of March 31st.

Next, it subtracts the weekday from March 31st to get the
timestamp for the last Sunday of March, and again uses the
time.localtime function to get the date of the last Sunday
of March. Finally, it returns the date.

The code then gets the current year using time.localtime and
calls the last_sunday_of_march function to get the date of the
last Sunday of March of the current year. The date is then 
printed in the format "Last Sunday of March %d: %d-%02d-%02d", 
where %d is replaced by the year and the date components (year,
month, and day).

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
