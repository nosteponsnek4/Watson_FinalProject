import pygame.draw
import pygame
from pygame.sprite import Sprite
from Ship_two import ShipTwo


class Bullet_Two(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game, i):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color_t
        self.ship = ShipTwo(ai_game)
        self.i = i

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_height,
                                self.settings.bullet_width)
        if self.i % 4 == 0:
            self.rect.midright = ai_game.ship_two.rect.midright
        elif self.i % 4 == 2:
            self.rect.midleft = ai_game.ship_two.rect.midleft
        elif self.i % 4 == 1:
            self.rect.midtop = ai_game.ship_two.rect.midtop
            self.rect.x += 8

        elif self.i % 4 == 3:
            self.rect.midbottom = ai_game.ship_two.rect.midbottom
            self.rect.x += 8

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""

        self.ship.update()
        if self.i % 4 == 0:
            self.x += self.settings.bullet_speed
        elif self.i % 4 == 2:
            self.x -= self.settings.bullet_speed
        elif self.i % 4 == 3:
            self.y -= self.settings.bullet_speed
        elif self.i % 4 == 1:
            self.y += self.settings.bullet_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.circle(self.screen, self.color, (self.rect.x, self.rect.y),
                           self.settings.bullet_radius, 0)