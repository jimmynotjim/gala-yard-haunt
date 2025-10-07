"""
Type stubs for pygame - for development on non-Pi systems.

These stubs allow type checking and IDE support when developing
on systems without the actual pygame library installed.
"""

from collections.abc import Sequence
from typing import Any

# Constants
QUIT: int
KEYDOWN: int
KEYUP: int
MOUSEBUTTONDOWN: int
MOUSEBUTTONUP: int
MOUSEMOTION: int

K_ESCAPE: int
K_SPACE: int
K_RETURN: int
K_UP: int
K_DOWN: int
K_LEFT: int
K_RIGHT: int
K_a: int
K_b: int
K_c: int
K_d: int
K_e: int
K_f: int
K_g: int
K_h: int
K_i: int
K_j: int
K_k: int
K_l: int
K_m: int
K_n: int
K_o: int
K_p: int
K_q: int
K_r: int
K_s: int
K_t: int
K_u: int
K_v: int
K_w: int
K_x: int
K_y: int
K_z: int

class Color:
    """Represents a color with RGBA values."""

    def __init__(self, r: int, g: int = 0, b: int = 0, a: int = 255) -> None: ...
    r: int
    g: int
    b: int
    a: int

class Rect:
    """Represents a rectangular area."""

    def __init__(self, left: int, top: int, width: int, height: int) -> None: ...
    x: int
    y: int
    width: int
    height: int
    left: int
    top: int
    right: int
    bottom: int
    centerx: int
    centery: int
    center: tuple[int, int]
    size: tuple[int, int]
    def colliderect(self, rect: Rect) -> bool: ...
    def collidepoint(self, x: int, y: int) -> bool: ...
    def copy(self) -> Rect: ...
    def move(self, x: int, y: int) -> Rect: ...

class Surface:
    """Represents an image or drawing surface."""

    def __init__(
        self,
        size: tuple[int, int],
        flags: int = 0,
        depth: int = 0,
    ) -> None: ...
    def fill(self, color: Color | tuple[int, int, int] | tuple[int, int, int, int]) -> Rect: ...
    def blit(
        self,
        source: Surface,
        dest: tuple[int, int] | Rect,
        area: Rect | None = None,
    ) -> Rect: ...
    def convert(self) -> Surface: ...
    def convert_alpha(self) -> Surface: ...
    def get_rect(self, **kwargs: Any) -> Rect: ...
    def get_width(self) -> int: ...
    def get_height(self) -> int: ...
    def get_size(self) -> tuple[int, int]: ...
    def set_colorkey(self, color: Color | tuple[int, int, int] | None, flags: int = 0) -> None: ...
    def set_alpha(self, value: int | None, flags: int = 0) -> None: ...

class Clock:
    """Manages timing and frame rate."""

    def __init__(self) -> None: ...
    def tick(self, framerate: int = 0) -> int: ...
    def tick_busy_loop(self, framerate: int = 0) -> int: ...
    def get_time(self) -> int: ...
    def get_fps(self) -> float: ...

class Event:
    """Represents a pygame event."""

    type: int
    dict: dict[str, Any]
    key: int
    pos: tuple[int, int]
    button: int

def init() -> tuple[int, int]:
    """Initialize all pygame modules."""
    ...

def quit() -> None:
    """Uninitialize all pygame modules."""
    ...

class display:
    """Module for controlling the display window."""

    @staticmethod
    def set_mode(
        size: tuple[int, int],
        flags: int = 0,
        depth: int = 0,
        display: int = 0,
    ) -> Surface: ...
    @staticmethod
    def flip() -> None: ...
    @staticmethod
    def update(rectangle: Rect | Sequence[Rect] | None = None) -> None: ...
    @staticmethod
    def set_caption(title: str, icontitle: str = '') -> None: ...
    @staticmethod
    def get_caption() -> tuple[str, str]: ...
    @staticmethod
    def get_surface() -> Surface: ...

class event:
    """Module for handling events."""

    @staticmethod
    def get() -> list[Event]: ...
    @staticmethod
    def poll() -> Event: ...
    @staticmethod
    def wait() -> Event: ...
    @staticmethod
    def pump() -> None: ...
    @staticmethod
    def clear(eventtype: int | Sequence[int] | None = None) -> None: ...

class time:
    """Module for monitoring time."""

    @staticmethod
    def get_ticks() -> int: ...
    @staticmethod
    def wait(milliseconds: int) -> int: ...
    @staticmethod
    def delay(milliseconds: int) -> int: ...
    @staticmethod
    def set_timer(event: int, millis: int) -> None: ...

Clock = Clock  # Re-export Clock class

class draw:
    """Module for drawing shapes."""

    @staticmethod
    def rect(
        surface: Surface,
        color: Color | tuple[int, int, int],
        rect: Rect | tuple[int, int, int, int],
        width: int = 0,
    ) -> Rect: ...
    @staticmethod
    def circle(
        surface: Surface,
        color: Color | tuple[int, int, int],
        center: tuple[int, int],
        radius: int,
        width: int = 0,
    ) -> Rect: ...
    @staticmethod
    def line(
        surface: Surface,
        color: Color | tuple[int, int, int],
        start_pos: tuple[int, int],
        end_pos: tuple[int, int],
        width: int = 1,
    ) -> Rect: ...
    @staticmethod
    def polygon(
        surface: Surface,
        color: Color | tuple[int, int, int],
        points: Sequence[tuple[int, int]],
        width: int = 0,
    ) -> Rect: ...

class font:
    """Module for loading and rendering fonts."""

    class Font:
        def __init__(self, filename: str | None, size: int) -> None: ...
        def render(
            self,
            text: str,
            antialias: bool,
            color: Color | tuple[int, int, int],
            background: Color | tuple[int, int, int] | None = None,
        ) -> Surface: ...
        def size(self, text: str) -> tuple[int, int]: ...

    @staticmethod
    def init() -> None: ...
    @staticmethod
    def get_default_font() -> str: ...
    @staticmethod
    def SysFont(name: str, size: int, bold: bool = False, italic: bool = False) -> Font: ...

class image:
    """Module for image transfer."""

    @staticmethod
    def load(filename: str) -> Surface: ...
    @staticmethod
    def save(surface: Surface, filename: str) -> None: ...

class mixer:
    """Module for loading and playing sounds."""

    class Sound:
        def __init__(self, filename: str | None) -> None: ...
        def play(self, loops: int = 0, maxtime: int = 0, fade_ms: int = 0) -> None: ...
        def stop(self) -> None: ...
        def set_volume(self, value: float) -> None: ...
        def get_volume(self) -> float: ...

    @staticmethod
    def init(
        frequency: int = 22050,
        size: int = -16,
        channels: int = 2,
        buffer: int = 512,
    ) -> None: ...
    @staticmethod
    def quit() -> None: ...
    @staticmethod
    def music() -> Any: ...

class key:
    """Module for working with the keyboard."""

    @staticmethod
    def get_pressed() -> Sequence[bool]: ...
    @staticmethod
    def name(key: int) -> str: ...
    @staticmethod
    def set_repeat(delay: int = 0, interval: int = 0) -> None: ...

class mouse:
    """Module for working with the mouse."""

    @staticmethod
    def get_pos() -> tuple[int, int]: ...
    @staticmethod
    def get_pressed() -> tuple[bool, bool, bool]: ...
    @staticmethod
    def set_visible(visible: bool) -> bool: ...
