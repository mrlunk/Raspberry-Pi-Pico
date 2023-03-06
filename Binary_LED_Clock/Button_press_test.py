"""
This code defines a button press handler function that detects when a button connected
to pin 27 is pressed and prevents double-clicks by ignoring button presses that occur
within 200 milliseconds of the last press.

Script by: MrLunk
https://github.com/mrlunk/Raspberry-Pi-Pico/
"""

import machine
import time

# define the button pin
button = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)

# define a function to handle button presses with protection against double-clicks
last_button_press_time = 0
last_button_pin = None

def handle_button_press(pin):
    global last_button_press_time
    global last_button_pin
    current_time = time.ticks_ms()
    if current_time - last_button_press_time > 200: # ignore button presses that occur within 500 milliseconds of the last press
        if last_button_pin == pin and current_time - last_button_press_time <= 1000: # check if the current button press is a double click
            print('Double click detected!')
        else:
            print('Button pressed!')
        last_button_pin = pin
        last_button_press_time = current_time


# attach the button press handler function to the button pin
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=handle_button_press)

# count up quick and print the current count to console to demonstrate running loop.
count = 0
while True:
    print(count)
    count += 1
    time.sleep(.2)
