import machine
import time

# set up buzzer on GPIO 28 to ground !
buzzer = machine.PWM(machine.Pin(28))

# set up frequency range and sweep duration
freq_range = range(100, 10001, 100)
sweep_duration = 10   # in seconds

# loop to sweep frequency from 100 to 10,000 Hz
start_time = time.time()
while time.time() - start_time < sweep_duration:
    for freq in freq_range:
        buzzer.freq(freq)   # set buzzer frequency
        buzzer.duty_u16(32767)   # set buzzer duty cycle to 50%
        time.sleep(0.01)    # wait for 10 milliseconds

# turn off buzzer
buzzer.duty_u16(0)
