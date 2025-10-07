"""
Basic LED blink example for Raspberry Pi.

This example blinks an LED connected to GPIO pin 17.
Press Ctrl+C to stop.

Wiring:
- LED positive (long leg) -> GPIO 17
- LED negative (short leg) -> 330Ω resistor -> Ground
"""

from time import sleep

from gpiozero import LED

# Configure LED on GPIO pin 17
led = LED(17)

print('Blinking LED on GPIO 17. Press Ctrl+C to stop.')

try:
    while True:
        led.on()
        print('LED ON')
        sleep(1)
        led.off()
        print('LED OFF')
        sleep(1)
except KeyboardInterrupt:
    print('\nStopping...')
finally:
    led.close()
    print('LED cleaned up.')
