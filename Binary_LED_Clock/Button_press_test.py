"""
trying to write code that detects and distinguishes 1 button short press, double click,
and hold button 3 sec.
Important is tht code should keep running !
"""

import machine
import time

# define the button pin
button = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)

# define a function to handle button presses
last_button_press_time = 0
last_button_pin = None

def handle_button_press(pin):
    global last_button_press_time
    global last_button_pin
    current_time = time.ticks_ms()
    # ignore button presses that occur within XXX milliseconds of the last press
    if current_time - last_button_press_time > 100:
        # check if the current button press is a double click
        if last_button_pin == pin and current_time - last_button_press_time <= 500:
            print('Double click detected!')
        else:
            # button held down for at least 3 seconds
            while not pin.value():
                if time.ticks_ms() - current_time >= 3000:
                    print('Button held for 3 seconds!')
                    break
            else:
                # button released before 3 seconds
                print('Button pressed!')
        last_button_pin = pin
        last_button_press_time = current_time

# attach the button press handler function to the button pin
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=handle_button_press)

# count up in seconds and print the current count
count = 0
while True:
    print(count)
    count += 1
    time.sleep(.2)

