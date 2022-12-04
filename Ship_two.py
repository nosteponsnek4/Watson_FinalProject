import pygame
import math
from time import sleep

class ship_two:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship2.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.angle = 90
        # Start each new ship at the bottom center of the screen.
        self.rect.midright = self.screen_rect.midright

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.turning_right = False
        self.turning_left = False
        self.accel = False
        self.i = 2

    def update(self):
        """Update the ship's position based on movement flags."""

        if self.turning_right:
            self.image = pygame.transform.rotate(self.image, -90)
            self.i += 1
            sleep(.35)

        if self.turning_left:
            self.image = pygame.transform.rotate(self.image, 90)
            self.i -= 1
            sleep(.35)

        if self.accel:
            if self.i % 4 == 0:
                self.x += self.settings.ship_speed
            elif self.i % 4 == 2:
                self.x -= self.settings.ship_speed
            elif self.i % 4 == 1:
                self.y += self.settings.ship_speed
            elif self.i % 4 == 3:
                self.y -= self.settings.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
