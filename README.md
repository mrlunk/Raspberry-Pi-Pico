# Raspberry Pi Pico
 Some Pi pico MicroPython scripts...

# Hello :)
 
## DST_Daylight_Saving_Time_correction_example.py

This code is written in MicroPython for the Raspberry Pi Pico, and its purpose is to correct the time for daylight saving time (DST).

1. The code starts by importing the time module.

2. Two functions, last_sunday_of_march(year) and last_sunday_of_oktober(year), are defined to calculate the last Sunday of March and October for a given year, respectively.

3. The current year is obtained using the time.localtime() function, and the dates for the last Sunday of March and October are calculated by calling the last_sunday_of_march() and last_sunday_of_oktober() functions.

4. The if statements then check if the current date is between the start date and end date of DST. If so, the DST_Adjustment is set to 1 hour. If the current date is not between the start and end date of DST, DST_Adjustment is set to 0.

5. The current time is obtained using time.localtime(), and the time tuple is converted to a list. The fourth element of the list (representing the hour) is then subtracted by DST_Adjustment (1 or 0) to correct for DST. The list is then converted back into a tuple, which is the final corrected time.

6. The final corrected time is then printed to the console.
 
 
 
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
