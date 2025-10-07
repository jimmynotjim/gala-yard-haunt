"""
Button input example for Raspberry Pi.

This example demonstrates reading a button press and controlling an LED.
Press the button to toggle the LED on/off.

Wiring:
- Button: One side -> GPIO 23, other side -> Ground
- LED positive (long leg) -> GPIO 17
- LED negative (short leg) -> 330Ω resistor -> Ground

Note: The button uses internal pull-up resistor, so it reads HIGH when not pressed
and LOW when pressed.
"""

from signal import pause

from gpiozero import LED, Button

# Configure components
led = LED(17)
button = Button(23)

print('Button example running. Press the button to toggle LED.')
print('Press Ctrl+C to stop.')


def toggle_led() -> None:
    """Toggle the LED state when button is pressed."""
    led.toggle()
    status = 'ON' if led.is_lit else 'OFF'
    print(f'Button pressed! LED is now {status}')


# Set up button press event
button.when_pressed = toggle_led

try:
    # Keep the program running
    pause()
except KeyboardInterrupt:
    print('\nStopping...')
finally:
    led.close()
    button.close()
    print('Cleaned up.')
