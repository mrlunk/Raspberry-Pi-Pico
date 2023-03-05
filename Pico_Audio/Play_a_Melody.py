# Buzzer on gpio 28 to groud.

import machine
import time

# Define the notes for the melody
melody = [
  262, 262, 392, 392, 440, 440, 392, 0,
  349, 349, 330, 330, 294, 294, 262, 0,
  392, 392, 349, 349, 330, 330, 294, 0,
  392, 392, 349, 349, 330, 330, 294, 0,
  262, 262, 392, 392, 440, 440, 392, 0,
  349, 349, 330, 330, 294, 294, 262, 0
]

# Set up the buzzer on GPIO 28
buzzer_pin = machine.Pin(28, machine.Pin.OUT)
buzzer = machine.PWM(buzzer_pin)

# Play the melody
for note in melody:
    if note == 0:
        buzzer.duty_u16(0)
    else:
        buzzer.freq(note)
        buzzer.duty_u16(32767)
    time.sleep(0.2)

# Turn off the buzzer
buzzer.deinit()

