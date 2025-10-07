"""
Type stubs for RPi.GPIO - for development on non-Pi systems.

These stubs allow type checking and IDE support when developing
on systems without the actual RPi.GPIO library installed.
"""

from collections.abc import Callable, Sequence
from typing import Any, Literal

# Board mode constants
BCM: int
BOARD: int

# Pin direction constants
OUT: int
IN: int

# Pin state constants
HIGH: int
LOW: int

# Pull up/down constants
PUD_UP: int
PUD_DOWN: int
PUD_OFF: int

# Edge detection constants
RISING: int
FALLING: int
BOTH: int

# PWM constants
UNKNOWN: int
HARD_PWM: int

# Version info
VERSION: str
RPI_INFO: dict[str, Any]
RPI_REVISION: int

def setmode(mode: Literal[11, 10]) -> None:
    """
    Set up numbering mode to use for channels.

    Args:
        mode: BOARD or BCM
    """
    ...

def getmode() -> int | None:
    """
    Get numbering mode used for channel numbers.

    Returns:
        BOARD, BCM, or None if not set
    """
    ...

def setwarnings(value: bool) -> None:
    """
    Enable or disable warning messages.

    Args:
        value: True to enable warnings, False to disable
    """
    ...

def setup(
    channel: int | Sequence[int],
    direction: int,
    pull_up_down: int = PUD_OFF,
    initial: int = LOW,
) -> None:
    """
    Set up a GPIO channel or list of channels with a direction and (optional) pull/up down control.

    Args:
        channel: GPIO channel number(s) based on the numbering mode
        direction: IN or OUT
        pull_up_down: PUD_OFF (default), PUD_UP or PUD_DOWN
        initial: Initial value for an output channel
    """
    ...

def cleanup(channel: int | Sequence[int] | None = None) -> None:
    """
    Clean up GPIO channels at the end of the program.

    Args:
        channel: Individual channel or list of channels to clean up.
                If None, clean up all channels used.
    """
    ...

def output(channel: int | Sequence[int], value: int | Sequence[int]) -> None:
    """
    Output to a GPIO channel or list of channels.

    Args:
        channel: GPIO channel number(s) based on the numbering mode
        value: HIGH or LOW (or list of values for multiple channels)
    """
    ...

def input(channel: int) -> int:
    """
    Read the value of a GPIO pin.

    Args:
        channel: GPIO channel number based on the numbering mode

    Returns:
        HIGH or LOW
    """
    ...

def wait_for_edge(
    channel: int,
    edge: int,
    bouncetime: int | None = None,
    timeout: int | None = None,
) -> int | None:
    """
    Wait for an edge.

    Args:
        channel: GPIO channel number based on the numbering mode
        edge: RISING, FALLING or BOTH
        bouncetime: Minimum time in ms between edge detections
        timeout: Timeout in ms. If None, wait indefinitely

    Returns:
        Channel number or None on timeout
    """
    ...

def add_event_detect(
    channel: int,
    edge: int,
    callback: Callable[[int], None] | None = None,
    bouncetime: int | None = None,
) -> None:
    """
    Enable edge detection events for a particular GPIO channel.

    Args:
        channel: GPIO channel number based on the numbering mode
        edge: RISING, FALLING or BOTH
        callback: Function to call when edge is detected (takes channel as argument)
        bouncetime: Minimum time in ms between edge detections
    """
    ...

def remove_event_detect(channel: int) -> None:
    """
    Remove edge detection for a particular GPIO channel.

    Args:
        channel: GPIO channel number based on the numbering mode
    """
    ...

def event_detected(channel: int) -> bool:
    """
    Check if an edge has occurred on a GPIO channel.

    Args:
        channel: GPIO channel number based on the numbering mode

    Returns:
        True if an event was detected since last call
    """
    ...

def add_event_callback(channel: int, callback: Callable[[int], None]) -> None:
    """
    Add a callback for an event already defined using add_event_detect().

    Args:
        channel: GPIO channel number based on the numbering mode
        callback: Function to call when edge is detected (takes channel as argument)
    """
    ...

def gpio_function(channel: int) -> int:
    """
    Return the current GPIO function (IN, OUT, PWM, SERIAL, I2C, SPI).

    Args:
        channel: GPIO channel number based on the numbering mode

    Returns:
        Function constant
    """
    ...

class PWM:
    """
    Pulse Width Modulation class.

    Example:
        p = GPIO.PWM(channel, frequency)
        p.start(duty_cycle)
    """

    def __init__(self, channel: int, frequency: float) -> None:
        """
        Initialize PWM on a channel.

        Args:
            channel: GPIO channel number based on the numbering mode
            frequency: PWM frequency in Hz
        """
        ...

    def start(self, duty_cycle: float) -> None:
        """
        Start PWM output.

        Args:
            duty_cycle: Duty cycle between 0.0 and 100.0
        """
        ...

    def stop(self) -> None:
        """Stop PWM output."""
        ...

    def ChangeDutyCycle(self, duty_cycle: float) -> None:
        """
        Change the duty cycle.

        Args:
            duty_cycle: Duty cycle between 0.0 and 100.0
        """
        ...

    def ChangeFrequency(self, frequency: float) -> None:
        """
        Change the frequency.

        Args:
            frequency: PWM frequency in Hz
        """
        ...
