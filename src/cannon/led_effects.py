#!/usr/bin/env python3
"""
LED Effects Module
Handles all WS2812B LED strip effects
"""

import time

from rpi_ws281x import Color, PixelStrip


class LEDController:
    def __init__(self, *, led_count: int = 30, led_pin: int = 18, brightness: int = 255) -> None:
        """Initialize the LED strip"""
        self.LED_COUNT = led_count
        self.LED_PIN = led_pin
        self.LED_BRIGHTNESS = brightness

        # LED strip configuration
        #
        # WS2812B chips are designed to receive data at 800kHz
        LED_FREQ_HZ = 800000
        # DMA allows the Pi to send data to the LEDs without using the CPU for every single bit
        # Channel 10 is the default safe choice for Raspberry Pi
        # Don't change unless you have conflicts with other hardware using DMA
        LED_DMA = 10
        # This controls whether the data signal is inverted (flipped upside-down electrically).
        # False = Normal signal (HIGH = 1, LOW = 0)
        # True = Inverted signal (HIGH = 0, LOW = 1)
        LED_INVERT = False
        # The Raspberry Pi has two PWM (Pulse Width Modulation) channels. This selects which one to use for the LED data.
        # 0 = PWM channel 0 (GPIO 12, 18, 40, 52)
        # 1 = PWM channel 1 (GPIO 13, 19, 41, 45, 53)
        LED_CHANNEL = 0

        # Initialize LED strip
        self.strip = PixelStrip(
            self.LED_COUNT,
            self.LED_PIN,
            LED_FREQ_HZ,
            LED_DMA,
            LED_INVERT,
            self.LED_BRIGHTNESS,
            LED_CHANNEL,
        )

        self.strip.begin()
        self.clear()

    def set_all(self, color: int) -> None:
        """Set all LEDs to a specifc color"""
        # Loop through each pixel and set the color values
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
        # Update the display with the new values set in the loops
        self.strip.show()

    def clear(self) -> None:
        """Turn off all LEDs"""
        self.set_all(Color(0, 0, 0))

    def building_glow(self, duration: float = 1.5, speed: float = 20) -> None:
        """Create a building orange/red glow effect"""
        steps = int(duration * speed)
        for step in range(steps):
            red = int((step / steps) * 255)
            green = int((1 - step / steps) * 10)
            color = Color(red, green, 0)
            self.set_all(color)
            time.sleep(duration / steps)

    def flash_explosion(self, duration: float = 0.3) -> None:
        """Bright white flash for explosion"""
        self.set_all(Color(255, 255, 255))
        time.sleep(duration)

    def fade_out(self, duration: float = 0.5, speed: float = 20) -> None:
        """Fade LEDs to black"""
        steps = int(duration * speed)
        for step in range(steps, -1, -1):
            brightness = int((step / steps) * 255)
            color = Color(brightness, brightness // 3, 0)
            self.set_all(color)
            time.sleep(duration / steps)
        self.clear()

    def pulse_status(self, color: int, times: int = 3) -> None:
        """Pulse LEDs to indicate status"""
        for _ in range(times):
            self.set_all(color)
            time.sleep(0.2)
            self.clear()
            time.sleep(0.2)
