class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 900
        self.bg_color = (30, 30, 30)

        # Ship settings
        self.ship_speed = 5
        self.shield_r = 30

        # Bullet settings
        self.bullet_speed = 15
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_radius = 5
        self.bullet_color_o = (180, 170, 70)
        self.bullet_color_t = (70, 170, 170)
        self.bullets_allowed = 2
