"""Type stubs for rpi_ws281x library."""

from typing import overload

@overload
def Color(red: int, green: int, blue: int) -> int:
    """
    Convert the provided red, green, blue color to a 24-bit color value.
    Each color component should be a value from 0 to 255 where 0 is the
    lowest intensity and 255 is the highest intensity.
    """
    ...

@overload
def Color(red: int, green: int, blue: int, white: int) -> int:
    """
    Convert the provided red, green, blue, white color to a 24-bit color value.
    Each color component should be a value from 0 to 255 where 0 is the
    lowest intensity and 255 is the highest intensity.
    """
    ...

class PixelStrip:
    """
    WS281x LED strip implementation.
    """

    def __init__(
        self,
        num: int,
        pin: int,
        freq_hz: int = 800000,
        dma: int = 10,
        invert: bool = False,
        brightness: int = 255,
        channel: int = 0,
        strip_type: int | None = None,
        gamma: list[int] | None = None,
    ) -> None:
        """
        Initialize the LED strip.

        Args:
            num: Number of LED pixels
            pin: GPIO pin connected to the pixels (must support PWM)
            freq_hz: LED signal frequency in hertz (usually 800000)
            dma: DMA channel to use for generating signal (try 10)
            invert: True to invert the signal (when using NPN transistor level shift)
            brightness: Set to 0 for darkest and 255 for brightest
            channel: PWM channel; set to 0 or 1
            strip_type: LED strip type (use module constants like ws.WS2811_STRIP_RGB)
            gamma: Gamma correction table
        """
        ...

    def begin(self) -> None:
        """
        Initialize library, must be called once before other functions.
        Raises RuntimeError if initialization fails.
        """
        ...

    def show(self) -> None:
        """Update the display with the data from the LED buffer."""
        ...

    def setPixelColor(self, n: int, color: int) -> None:
        """
        Set LED at position n to the provided 24-bit color value.

        Args:
            n: LED position (0-indexed)
            color: 24-bit RGB color value
        """
        ...

    def setPixelColorRGB(self, n: int, red: int, green: int, blue: int, white: int = 0) -> None:
        """
        Set LED at position n to the provided red, green, blue color.

        Args:
            n: LED position (0-indexed)
            red: Red component (0-255)
            green: Green component (0-255)
            blue: Blue component (0-255)
            white: White component for RGBW strips (0-255)
        """
        ...

    def setBrightness(self, brightness: int) -> None:
        """
        Set the brightness of all pixels.

        Args:
            brightness: Brightness value (0-255)
        """
        ...

    def getBrightness(self) -> int:
        """Get the current brightness value."""
        ...

    def getPixels(self) -> int:
        """Return the pixels buffer."""
        ...

    def numPixels(self) -> int:
        """Return the number of pixels in the strip."""
        ...

    def getPixelColor(self, n: int) -> int:
        """
        Get the 24-bit RGB color value for the LED at position n.

        Args:
            n: LED position (0-indexed)

        Returns:
            24-bit color value
        """
        ...

    def getPixelColorRGB(self, n: int) -> tuple[int, int, int, int]:
        """
        Get the red, green, blue, white color values for the LED at position n.

        Args:
            n: LED position (0-indexed)

        Returns:
            Tuple of (red, green, blue, white) values
        """
        ...

class Adafruit_NeoPixel(PixelStrip):
    """Alias for PixelStrip for backwards compatibility."""

    ...

# Strip types
WS2811_STRIP_RGB: int
WS2811_STRIP_RBG: int
WS2811_STRIP_GRB: int
WS2811_STRIP_GBR: int
WS2811_STRIP_BRG: int
WS2811_STRIP_BGR: int
WS2812_STRIP: int
SK6812_STRIP_RGBW: int
SK6812_STRIP_RBGW: int
SK6812_STRIP_GRBW: int
SK6812_STRIP_GBRW: int
SK6812_STRIP_BRGW: int
SK6812_STRIP_BGRW: int
SK6812W_STRIP: int
