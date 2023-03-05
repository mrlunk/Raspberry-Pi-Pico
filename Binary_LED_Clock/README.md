
Rough basic but working code. UNDER DEVLOPMENT 3/5/2023

NTP timesynced Binary LED clock

Scipt in Micropython for Raspberry Pi Pico W.

Script by: MrLunk

Link: https://github.com/mrlunk/Raspberry-Pi-Pico/edit/main/Binary_LED_Clock/

![image](https://user-images.githubusercontent.com/25208554/222953650-ffcc8cbb-c6f3-461f-9d17-29f5336d6641.png)


Remove:


To be added:
- NTP stimesync every 24 hours
- Daylight savings time adjustment
- Reset button
- 12 / 24 hour clock switchable
- LED mode 'breathing' transitions (pulsating)
- LED mode Steady light bright/medium/low
- auto adjust brightness day/night (lightsensor ?)
- external html website with info about the project hosted on the pico W too.
- etc...
- 
Script by MrLunk 2023
https://github.com/mrlunk

_______________________________________________________________________________

# The script sofar: 3/5/2023

This script demonstrates how to use the Raspberry Pi Pico's built-in Wi-Fi module and GPIO pins to create a simple clock that displays the time in binary format using LEDs.

The script uses the board's built-in Wi-Fi module to connect to a wireless network, and then synchronizes the board's internal clock with the Network Time Protocol (NTP) server to obtain accurate time information. The script also uses the board's General Purpose Input/Output (GPIO) pins to control several LEDs, displaying the current time in binary format.

Here is a breakdown of the script:

1. The first few lines of the script import the necessary libraries and modules, including machine, network, time, ntptime, and utime.

2. The next few lines of the script define some variables, including the Wi-Fi network's SSID and password, as well as lists of GPIO pins that will be used to control the LEDs.

3. The next section of the script sets up the GPIO pins for output and defines several functions for displaying the current time in binary format on the LEDs.

4. The connect_wifi() function attempts to connect the board to the Wi-Fi network using the specified SSID and password. It waits up to 10 seconds for the connection to be established, and if it fails, raises an error. If the connection is successful, it prints the board's IP address to the console.

5. The Wifi_time_sync() function synchronizes the board's internal clock with the NTP server to obtain accurate time information. It first gets the WLAN object and then uses the ntptime module to set the time. Finally, it deinitializes the WLAN object to free up system resources.

6. The main loop of the script starts by calling the connect_wifi() and Wifi_time_sync() functions to connect to the Wi-Fi network and synchronize the time.

7. Inside the main loop, the current hour, minute, and second are obtained using the time.localtime() function, and then the dispBinarySec(), dispBinaryMin(), and dispBinaryHr() functions are called to display the current time in binary format on the LEDs.

8. The script also checks if the current time is midnight (countH == 0 and countM == 0 and countS == 0), and if so, calls the connect_wifi() and Wifi_time_sync() functions again to re-sync the clock with the NTP server.

9. The last line of the main loop uses the utime.sleep() function to pause the script for 1 second before repeating the loop again.


