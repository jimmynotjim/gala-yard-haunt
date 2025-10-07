"""
Type stubs for gpiozero - for development on non-Pi systems.

These stubs allow type checking and IDE support when developing
on systems without the actual gpiozero library installed.
"""

from collections.abc import Callable

class LED:
    """Represents a light emitting diode (LED)."""

    def __init__(
        self,
        pin: int,
        active_high: bool = True,
        initial_value: bool = False,
        pin_factory: object | None = None,
    ) -> None: ...
    def on(self) -> None:
        """Turn the LED on."""
        ...

    def off(self) -> None:
        """Turn the LED off."""
        ...

    def toggle(self) -> None:
        """Toggle the LED state."""
        ...

    def blink(
        self,
        on_time: float = 1,
        off_time: float = 1,
        n: int | None = None,
        background: bool = True,
    ) -> None:
        """Make the LED blink on and off repeatedly."""
        ...

    def pulse(
        self,
        fade_in_time: float = 1,
        fade_out_time: float = 1,
        n: int | None = None,
        background: bool = True,
    ) -> None:
        """Make the LED fade in and out repeatedly."""
        ...

    def close(self) -> None:
        """Shut down the device and release all associated resources."""
        ...

    @property
    def is_lit(self) -> bool:
        """Returns True if the LED is currently on."""
        ...

    @property
    def value(self) -> float:
        """The duty cycle of the LED. 0.0 is off, 1.0 is fully on."""
        ...

    @value.setter
    def value(self, value: float) -> None: ...
    @property
    def pin(self) -> object:
        """The Pin that the LED is connected to."""
        ...

class Button:
    """Represents a simple push button or switch."""

    def __init__(
        self,
        pin: int,
        pull_up: bool = True,
        active_state: bool | None = None,
        bounce_time: float | None = None,
        hold_time: float = 1,
        hold_repeat: bool = False,
        pin_factory: object | None = None,
    ) -> None: ...
    def wait_for_press(self, timeout: float | None = None) -> bool:
        """Pause the script until the button is pressed."""
        ...

    def wait_for_release(self, timeout: float | None = None) -> bool:
        """Pause the script until the button is released."""
        ...

    def close(self) -> None:
        """Shut down the device and release all associated resources."""
        ...

    @property
    def is_pressed(self) -> bool:
        """Returns True if the button is currently pressed."""
        ...

    @property
    def is_held(self) -> bool:
        """Returns True if the button has been held for hold_time."""
        ...

    @property
    def pin(self) -> object:
        """The Pin that the button is connected to."""
        ...

    when_pressed: Callable[[], None] | None
    when_released: Callable[[], None] | None
    when_held: Callable[[], None] | None

class PWMLED(LED):
    """Represents a light emitting diode (LED) with PWM control."""

    def __init__(
        self,
        pin: int,
        active_high: bool = True,
        initial_value: float = 0,
        frequency: int = 100,
        pin_factory: object | None = None,
    ) -> None: ...

class RGBLED:
    """Represents a full color RGB LED."""

    def __init__(
        self,
        red: int,
        green: int,
        blue: int,
        active_high: bool = True,
        initial_value: tuple[float, float, float] = (0, 0, 0),
        pwm: bool = True,
        pin_factory: object | None = None,
    ) -> None: ...
    def on(self) -> None: ...
    def off(self) -> None: ...
    def toggle(self) -> None: ...
    def close(self) -> None: ...
    @property
    def is_lit(self) -> bool: ...
    @property
    def value(self) -> tuple[float, float, float]: ...
    @value.setter
    def value(self, value: tuple[float, float, float]) -> None: ...
    @property
    def color(self) -> tuple[float, float, float]: ...
    @color.setter
    def color(self, value: tuple[float, float, float]) -> None: ...

class Servo:
    """Represents a PWM-controlled servo motor."""

    def __init__(
        self,
        pin: int,
        initial_value: float = 0,
        min_pulse_width: float = 1 / 1000,
        max_pulse_width: float = 2 / 1000,
        frame_width: float = 20 / 1000,
        pin_factory: object | None = None,
    ) -> None: ...
    def min(self) -> None:
        """Set the servo to its minimum position."""
        ...

    def mid(self) -> None:
        """Set the servo to its mid-point position."""
        ...

    def max(self) -> None:
        """Set the servo to its maximum position."""
        ...

    def close(self) -> None: ...
    @property
    def value(self) -> float | None: ...
    @value.setter
    def value(self, value: float | None) -> None: ...

class Motor:
    """Represents a generic motor connected to a motor controller."""

    def __init__(
        self,
        forward: int,
        backward: int,
        enable: int | None = None,
        pwm: bool = True,
        pin_factory: object | None = None,
    ) -> None: ...
    def forward(self, speed: float = 1) -> None:
        """Drive the motor forwards."""
        ...

    def backward(self, speed: float = 1) -> None:
        """Drive the motor backwards."""
        ...

    def reverse(self) -> None:
        """Reverse the current direction of the motor."""
        ...

    def stop(self) -> None:
        """Stop the motor."""
        ...

    def close(self) -> None: ...
    @property
    def value(self) -> float: ...
    @value.setter
    def value(self, value: float) -> None: ...
    @property
    def is_active(self) -> bool: ...

class DistanceSensor:
    """Represents an HC-SR04 ultrasonic distance sensor."""

    def __init__(
        self,
        echo: int,
        trigger: int,
        queue_len: int = 30,
        max_distance: float = 1,
        threshold_distance: float = 0.3,
        partial: bool = False,
        pin_factory: object | None = None,
    ) -> None: ...
    def wait_for_in_range(self, timeout: float | None = None) -> bool: ...
    def wait_for_out_of_range(self, timeout: float | None = None) -> bool: ...
    def close(self) -> None: ...
    @property
    def distance(self) -> float:
        """Returns the current distance in meters."""
        ...

    @property
    def max_distance(self) -> float: ...
    @property
    def threshold_distance(self) -> float: ...
    @threshold_distance.setter
    def threshold_distance(self, value: float) -> None: ...

    when_in_range: Callable[[], None] | None
    when_out_of_range: Callable[[], None] | None

class MotionSensor:
    """Represents a passive infra-red (PIR) motion sensor."""

    def __init__(
        self,
        pin: int,
        queue_len: int = 1,
        sample_rate: float = 10,
        threshold: float = 0.5,
        partial: bool = False,
        pin_factory: object | None = None,
    ) -> None: ...
    def wait_for_motion(self, timeout: float | None = None) -> bool: ...
    def wait_for_no_motion(self, timeout: float | None = None) -> bool: ...
    def close(self) -> None: ...
    @property
    def motion_detected(self) -> bool: ...

    when_motion: Callable[[], None] | None
    when_no_motion: Callable[[], None] | None

class LightSensor:
    """Represents a light dependent resistor (LDR)."""

    def __init__(
        self,
        pin: int,
        queue_len: int = 5,
        charge_time_limit: float = 0.01,
        threshold: float = 0.1,
        partial: bool = False,
        pin_factory: object | None = None,
    ) -> None: ...
    def wait_for_light(self, timeout: float | None = None) -> bool: ...
    def wait_for_dark(self, timeout: float | None = None) -> bool: ...
    def close(self) -> None: ...
    @property
    def light_detected(self) -> bool: ...
    @property
    def value(self) -> float: ...

    when_light: Callable[[], None] | None
    when_dark: Callable[[], None] | None

class Buzzer:
    """Represents a digital buzzer component."""

    def __init__(
        self,
        pin: int,
        active_high: bool = True,
        initial_value: bool = False,
        pin_factory: object | None = None,
    ) -> None: ...
    def on(self) -> None: ...
    def off(self) -> None: ...
    def toggle(self) -> None: ...
    def beep(
        self,
        on_time: float = 1,
        off_time: float = 1,
        n: int | None = None,
        background: bool = True,
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def is_active(self) -> bool: ...
    @property
    def value(self) -> float: ...

def pause() -> None:
    """Pause the script indefinitely (until interrupted by Ctrl+C)."""
    ...
