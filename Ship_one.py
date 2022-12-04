import pygame
import math
import time

class ship_one:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship1.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.i = 0


        # Movement flags
        self.turning_right = False
        self.turning_left = False
        self.accel = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Need to write the movement and turn codes here (similar control scheme to alien game)

        if self.turning_right:
            self.image = pygame.transform.rotate(self.image, -90)
            self.i += 1
            time.sleep(.35)

        if self.turning_left:
            self.image = pygame.transform.rotate(self.image, 90)
            self.i -= 1
            time.sleep(.35)




        if self.accel:
            if self.i % 4 == 0:
                self.x += self.settings.ship_speed
            elif self.i % 4 == 2:
                self.x -= self.settings.ship_speed
            elif self.i % 4 == 1:
                self.y += self.settings.ship_speed
            elif self.i % 4 == 3:
                self.y -= self.settings.ship_speed


        # accelerates forwards (no backwards), and turns by degrees
        self.rect.x = self.x
        self.rect.y = self.y


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
