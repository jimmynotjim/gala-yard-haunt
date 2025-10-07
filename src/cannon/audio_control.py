#!/usr/bin/env python3
"""
Audio Control Module
Handles sound effects playback
"""

import os

import pygame


class AudioController:
    def __init__(self) -> None:
        """Initialize audio system"""
        pygame.mixer.init()
        # Get the directory where this file lives
        current_dir = os.path.dirname(os.path.abspath(__file__))
        audio_path = os.path.join(current_dir, 'cannon-fire.wav')
        self.explosion_sound = pygame.mixer.Sound(audio_path)

    def play_explosion(self) -> None:
        """Play explosion sound"""
        self.explosion_sound.play()

    def cleanup(self) -> None:
        """Shutdown audio system"""
        pygame.mixer.quit()
