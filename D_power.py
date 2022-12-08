import pygame
from random import randint
import pygame.draw
import pygame
from pygame.sprite import Sprite


class ShieldUp(Sprite):
    def __init__(self, df):
        super().__init__()
        pygame.init()

        self.screen = df.screen
        self.settings = df.settings
        self.screen_rect = df.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/Shield.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.x = randint(80, 1100)
        self.rect.y = randint(180, 500)

        self.color = (60, 120, 200)

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_shield(self):
        pygame.draw.circle(self.screen, self.color, (self.rect.x + 20, self.rect.y + 20),
                           self.settings.shield_r, 5)
        self.screen.blit(self.image, self.rect)

# Causes the shield image to appear at random times and places
# Adds one shield level to the ship that picks it up
