import pygame.draw
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.circle = pygame.draw.circle(self.screen, self.settings.bg_color, (0, 0),
                                         self.settings.bullet_radius, 0)
        self.circle.midtop = ai_game.ship.cicle.midtop

        # Store the bullet's position as a decimal value.
        self.y = float(self.circle.y)
        self.x = float(self.circle.x)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.circle.y = self.y
        self.circle.x =self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.circle(self.screen, self.settings.bg_color, (self.circle.x,self.circle.y),
                                         self.settings.bullet_radius, 0)