import pygame


class ShipTwo:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship2.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.angle = 90
        # Start each new ship at the bottom center of the screen.
        self.rect.midright = self.screen_rect.midright

        self.health = 5
        self.color = (60, 120, 200)

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.turning_right = False
        self.turning_left = False
        self.accel = False
        self.i = 2
        self.t = 0

    def update(self):
        """Update the ship's position based on movement flags."""

        if self.turning_right:
            if self.t == 0:
                self.image = pygame.transform.rotate(self.image, -90)
                self.i += 1
                self.t += 1

        elif self.turning_left:
            if self.t == 0:
                self.image = pygame.transform.rotate(self.image, 90)
                self.i -= 1
                self.t += 1
        else:
            self.t = 0

        if self.accel:
            if self.i % 4 == 0:
                if self.x <= 1140:
                    self.x += self.settings.ship_speed
            elif self.i % 4 == 2:
                if self.x >= 20:
                    self.x -= self.settings.ship_speed
            elif self.i % 4 == 1:
                if self.y <= 540:
                    self.y += self.settings.ship_speed
            elif self.i % 4 == 3:
                if self.y >= 50:
                    self.y -= self.settings.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y

        if self.health >= 4:
            self.color = (60, 120, 200)
        elif self.health >= 2:
            self.color = (200, 60, 60)
        elif self.health >= 0:
            self.color = self.settings.bg_color
        else:
            self.image = pygame.image.load('images/ded.png')
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.health = -5

    def blitme(self):
        """Draw the ship at its current location."""
        pygame.draw.circle(self.screen, self.color, (self.rect.x + 20, self.rect.y + 20),
                           self.settings.shield_r, 5)
        self.screen.blit(self.image, self.rect)
