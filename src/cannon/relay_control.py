#!/usr/bin/env python3
"""
Relay Control Module
Handles fog machine and fan relays
"""

from gpiozero import OutputDevice


class RelayController:
    def __init__(self, fog_pin: int = 17, fan_pin: int = 27) -> None:
        """Initialize relay pins using gpiozero"""

        self.fog_relay: OutputDevice = OutputDevice(fog_pin, active_high=True, initial_value=False)
        self.fan_relay: OutputDevice = OutputDevice(fan_pin, active_high=True, initial_value=False)

    def fog_on(self) -> None:
        """Turn on fog machine"""
        self.fog_relay.on()

    def fog_off(self) -> None:
        """Turn off fog machine"""
        self.fog_relay.off()

    def fan_on(self) -> None:
        """Turn on fan"""
        self.fan_relay.on()

    def fan_off(self) -> None:
        """Turn off fan"""
        self.fan_relay.off()

    def cleanup(self) -> None:
        """Turn off all relays"""
        self.fog_off()
        self.fan_off()

    def __del__(self) -> None:
        """Cleanup when object is destroyed"""
        self.cleanup()
