import sys
import pygame

from Settings import Settings
from Ship_two import ship_two
from Ship_one import ship_one
from Bullet import Bullet

class Dogfighter:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((1200, 600))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship_one = ship_one(self)
        self.ship_two = ship_two(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship_one.update()
            self.ship_two.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship_two.turning_right = True
        elif event.key == pygame.K_LEFT:
            self.ship_two.turning_left = True
        elif event.key == pygame.K_UP:
            self.ship_two.accel = True
        # Need help adding the acceleration for ship two
        # Need help creating the keydown events for ship one using WAD keys
        if event.key == pygame.K_d:
            self.ship_one.turning_right = True
        elif event.key == pygame.K_a:
            self.ship_one.turning_left = True
        elif event.key == pygame.K_w:
            self.ship_one.accel = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_DOWN:  # Need to split the fire mechanic
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship_two.turning_right = False
        elif event.key == pygame.K_LEFT:
            self.ship_two.turning_left = False
        elif event.key == pygame.K_UP:
            self.ship_two.accel = False
        if event.key == pygame.K_d:
            self.ship_one.turning_right = False
        elif event.key == pygame.K_a:
            self.ship_one.turning_left = False
        elif event.key == pygame.K_w:
            self.ship_one.accel = False
        # Need help adding the stop acceleration for ship two
        # Need help creating the keyup events for ship one using WAD keys

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        # Need to split fire mechanic
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.y <= 0:  # Need to change this so it removes at any edge
                self.bullets.remove(bullet)
            if bullet.rect.x <= 0:  # Need to change this so it removes at any edge
                self.bullets.remove(bullet)
            if bullet.rect.y >= 800:  # Need to change this so it removes at any edge
                self.bullets.remove(bullet)
            if bullet.rect.x >= 1200:  # Need to change this so it removes at any edge
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship_one.blitme()
        self.ship_two.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    df = Dogfighter()
    df.run_game()