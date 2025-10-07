"""
LED blink example with environment variables and type hints.

This example demonstrates best practices:
- Loading configuration from .env file
- Type hints for better code quality
- Proper error handling
- Resource cleanup

Setup:
1. Copy .env.example to .env
2. Update LED_PIN in .env if needed
3. Run: python examples/blink_env.py

Wiring:
- LED positive (long leg) -> GPIO pin (default: 17)
- LED negative (short leg) -> 330Ω resistor -> Ground
"""

import os
from time import sleep

from dotenv import load_dotenv
from gpiozero import LED

# Load environment variables from .env file
load_dotenv()


def blink_led(pin: int, interval: float = 1.0) -> None:
    """
    Blink an LED on the specified GPIO pin.

    Args:
        pin: GPIO pin number (BCM numbering)
        interval: Time in seconds between blinks

    Raises:
        ValueError: If pin number is invalid
    """
    if not 0 <= pin <= 27:
        raise ValueError(f'Invalid pin number: {pin}. Must be between 0 and 27.')

    led = LED(pin)
    print(f'Blinking LED on GPIO {pin} every {interval}s. Press Ctrl+C to stop.')

    try:
        while True:
            led.toggle()
            status = 'ON' if led.is_lit else 'OFF'
            print(f'LED {status}')
            sleep(interval)
    except KeyboardInterrupt:
        print('\nStopping...')
    finally:
        led.close()
        print('LED cleaned up.')


if __name__ == '__main__':
    # Get LED pin from environment variable, default to 17
    led_pin = int(os.getenv('LED_PIN', '17'))

    # Get blink interval from environment, default to 1 second
    blink_interval = float(os.getenv('BLINK_INTERVAL', '1.0'))

    blink_led(led_pin, blink_interval)
