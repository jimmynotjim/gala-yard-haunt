#!/usr/bin/env python3
"""
Halloween Cannon Controller - Main File
Coordinates all components using gpiozero
"""

import random
import threading
import time

from audio_control import AudioController
from gpiozero import Button
from led_effects import LEDController
from relay_control import RelayController
from rpi_ws281x import Color

# Config
BUTTON_PIN = 22
LED_COUNT = 30
MIN_WAIT = 30
MAX_WAIT = 120
FUSE_DURATION = 3.15
FOG_DURATION = 7.0
FAN_DURATION = 5.0
BUTTON_HOLD_TIME = 2.0
GLOW_DURATION = 1.5

# Global state
is_running = False
shutdown_flag = False

# Initialize controllers

leds = LEDController(led_count=LED_COUNT)
relays = RelayController()
audio = AudioController()
button = Button(BUTTON_PIN, pull_up=True, hold_time=BUTTON_HOLD_TIME)


def fire_cannon() -> None:
    """Execute complete cannon firing sequence"""
    if not is_running:
        return

    print('🎃 Firing cannon!')

    # 1. Start audio
    print('  - Starting fuse sound...')
    audio.play_explosion()

    # 2. Start Fog machine to build up smoke
    print('  - Fog ON')
    relays.fog_on()

    # 3. Building glow
    print('  - Building glow...')
    leds.building_glow(duration=GLOW_DURATION)

    if not is_running:
        return

    # 4. Wait for rest of fuse to burn
    remaining_fuse_time = FUSE_DURATION - GLOW_DURATION
    print(f'  - Fuse burning... ({remaining_fuse_time:.2f}s)')
    time.sleep(remaining_fuse_time)

    if not is_running:
        return

    # 5. Fan on to push smoke
    print('  - Fan ON')
    relays.fan_on()

    # 6. Flash LED at peak of sound effect
    print('  - BOOM!')
    leds.flash_explosion(duration=0.3)

    # 7. Keep fog running for FOG_DURATION
    remaining_fog_time = FOG_DURATION - FUSE_DURATION
    time.sleep(remaining_fog_time)

    # 8. Fog off
    print('  - Fog OFF')
    relays.fog_off()

    # 9. Fade LEDs
    leds.fade_out(duration=0.5)

    # 10. Keep fan running for remaining time
    remaining_fan_time = FAN_DURATION - remaining_fog_time
    time.sleep(remaining_fan_time)

    # 11. Fan off
    print('  - Fan OFF')
    relays.fan_off()

    print('  - Complete!/n')


def cannon_loop() -> None:
    """Main firing loop - runs in background thread"""
    global is_running

    while not shutdown_flag:
        if is_running:
            fire_cannon()

            if not is_running:
                break

            wait_time = random.randint(MIN_WAIT, MAX_WAIT)
            print(f'Waiting {wait_time} seconds...')

            # Wait in small increments so we can respond to stop quickly
            for _ in range(wait_time):
                if not is_running or shutdown_flag:
                    break
                time.sleep(1)

        else:
            time.sleep(0.1)


def toggle_cannon() -> None:
    """Toggle cannon on/off when button is held"""
    global is_running

    is_running = not is_running

    if is_running:
        print('\n' + '=' * 50)
        print('CANNON STARTED!')
        print('=' * 50)
        leds.pulse_status(Color(0, 255, 0), times=3)
    else:
        print('\n' + '=' * 50)
        print('CANNON STOPPED!')
        print('=' * 50)
        leds.pulse_status(Color(255, 0, 0), times=3)


def main() -> None:
    """Main program"""
    global shutdown_flag
    global is_running

    print('=' * 50)
    print('Halloween Cannon Controller')
    print('=' * 50)
    print('Press and hold button for 2 seconds to START/STOP')
    print('Press CTRL+C to exit')
    print('=' * 50)

    button.when_held = toggle_cannon

    cannon_thread = threading.Thread(target=cannon_loop, daemon=True)
    cannon_thread.start()

    try:
        # Keep main thread alive
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('\n\nShutting down...')

    finally:
        shutdown_flag = True
        is_running = False
        time.sleep(0.5)

        leds.clear()
        relays.cleanup()
        audio.cleanup()
        print('Cleanup complete')


if __name__ == '__main__':
    main()
