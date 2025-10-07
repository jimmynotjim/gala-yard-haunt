#!/usr/bin/env python3
"""
Audio Control Module
Handles sound effects playback
"""

import pygame


class AudioController:
    def __init__(self) -> None:
        """Initialize audio system"""
        pygame.mixer.init()
        self.explosion_sound = pygame.mixer.Sound('cannon-fire.wav')

    def play_explosion(self) -> None:
        """Play explosion sound"""
        self.explosion_sound.play()

    def cleanup(self) -> None:
        """Shutdown audio system"""
        pygame.mixer.quit()
