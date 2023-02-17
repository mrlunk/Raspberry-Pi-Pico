# Raspberry Pi Pico
 Some Pi pico MicroPython scripts...

Hello welcome to this humble little corner of github I can call 'mine'.

I am learning MicroPython and making a script for a binary clock that runs fully automatic.
1. clock should adjust for Daylight Savings Time when needed automatically.
2. clock should sync with NTP time server over Wifi every day at midnight

The files you encounter here are partial code / snippets of what needs to become the full script...

This is the way I learn... part by part and combining later...

Hope you enjoy some of my scripts.
AND please let me know if you spot flaws errors or mistakes :)

Be Well and Happy !

Greetings,

Peter Lunk



# Script descriptions

## NTP_synced_24h_Clock_with_DST_correction.py

This is a Raspberry pi Pico W Micro-Python script for a 24-hour clock that syncs with a network time server (NTP) every day at midnight (00:00:00). The clock also automatically adjusts for Daylight Saving Time (DST) in the Amsterdam (AMS) time zone.

The script imports the required libraries, including network, time, struct, ntptime, and machine. It then sets up the LED pin, SSID, and password for the Wi-Fi network.

The connect_wifi() function is defined to connect to the Wi-Fi network, while the Wifi_time_sync() function is used to sync the clock with the NTP server.

The last_sunday_of_month() function is used to calculate the last Sunday of the month for DST adjustments.

The Connect_and_sync() function is used to connect to the Wi-Fi network and sync the clock with the NTP server.

The script uses an infinite loop to continuously display the time and date. The DST_Adjustment variable is used to adjust the time for DST, and the final_time variable is used to store the adjusted time.

The Year, Month, Day, Hour, Minute, Second, DayOTWeek, and DayNumber variables are then used to display the time and date in the required format.
 
## DST_Daylight_Saving_Time_correction_example.py

This script is a python script that calculates the corrected current time taking into account Daylight Saving Time (DST).

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

## Metric_Clock.py

This code converts regular time (in hours, minutes, and seconds) to metric time (in metric hours, metric minutes, and metric seconds). Metric time uses a base 10 system instead of the base 60 system used in regular time.

The code first gets the number of seconds past midnight using the utime.time() function. It then calculates the decimal hours by dividing the number of seconds by 3600 (the number of seconds in an hour). It then converts decimal hours to metric time by multiplying by 100000 and dividing by 24. This gives us the number of metric seconds since midnight.

The metric time is then broken down into metric hours, metric minutes, and metric seconds using integer division and modulus operations.

The code then prints out both the metric time and regular time using the print() function. It also includes a 96ms delay using the utime.sleep_ms() function to make sure the code doesn't execute too quickly.

Metric Time information: https://en.wikipedia.org/wiki/Metric_time 

Metric time clock example: https://minkukel.com/en/clocks/metric-clock/ (not mine)

## Degrees_Time.py

This is a Python script that calculates the number of degrees that the Earth has turned since midnight, and continuously prints the result along with the current timestamp.

The script first sets the number of seconds per day and per degree, and then enters an infinite loop. Within the loop, it uses the time module to get the current time as a timestamp, calculates the number of seconds that have elapsed since midnight, and then converts that to the number of degrees that the Earth has turned by dividing by the number of seconds per degree.

It then prints out the result along with the current timestamp using the print function, and then waits for one second using the time.sleep function before starting the loop again.


Micropython scripts for Raspberry pi Pico By: MrLunk 2023
