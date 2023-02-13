# Raspberry Pi Pico
 Some Pi pico MicroPython scripts...

Hello welcome to this humble little corner of github I can call 'mine'.

I am learning MicroPython and making a script for a binary clock that runs fully automatic.
1. clock should adjust for Daylight Savings Time when needed automatically.
2. clock should sync with NTP time server over Wifi every day at midnight

The files you encounter here are partial code / snippets of what needs to become the full script...

This is the way I learn... part by part and combining later...

Hope you enjoy some of my scripts.

Be Well and Happy !

Greetings,

Peter Lunk



# Script descriptions
 
## DST_Daylight_Saving_Time_correction_example.py

This script is a python script that calculates the final corrected time taking into account Daylight Saving Time (DST).

1. Importing the time module: The time module is imported to use the functions provided by it.

2. Defining the last_sunday_of_month function: The function takes two arguments, year and month, and returns the date of the last Sunday of the given month and year.

3. Calculating the last Sunday of March and October: This is done by calling the last_sunday_of_month function twice with the current year and months 3 and 10. The result is stored in the variables DST_start_date and DST_end_date.

4. Getting the current date: The current date is obtained using the localtime function of the time module and storing the first three elements of the result in the current_date variable.

5. Calculating the DST adjustment: The script checks if the current date is between the last Sunday of March and the last Sunday of October. If it is, then the DST adjustment is set to 1 hour, otherwise, it is set to 0 hours.

6. Getting the current time: The current time is obtained using the localtime function of the time module and stored in the current_time variable.

7. Converting the current time to a list: The current time is converted to a list so that it can be modified.

8. Subtracting the DST adjustment from the current time: The hour component of the current time is subtracted by the DST adjustment.

9. Converting the modified time back to a tuple: The modified list is converted back to a tuple.

10. Printing the final corrected time: The final corrected time is printed.
 
 
 
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
