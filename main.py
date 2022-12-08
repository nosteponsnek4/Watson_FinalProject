import sys
import pygame

from Settings import Settings
from Ship_two import ShipTwo
from ShipOne import ShipOne
from Bullet import Bullet
from Bullet_two import Bullet_Two


class Dogfighter:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        pygame.mixer.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((1200, 600))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.base_font = pygame.font.Font(None, 40)
        self.start_txt = 'Press "P" to Start'
        self.inst_txt = 'Press "I" for instructions'
        self.P_one_instruction_txt = 'Player one: W- Forward, A- Turn Right, D-Turn Left, S-Fire'
        self.P_two_instruction_txt = 'Player two: Up- Forward, Right- Turn Right, Left-Turn Left, Down-Fire'
        self.Rules_txt = "Each shield absorbs two shots"
        self.Rules_two_txt = "Once all shields are depleted your ship is vulnerable"
        self.ded_txt = 'Winner!!!'
        self.txt_rect = pygame.Rect(100, 110, 120, 55)

        self.ship_one = ShipOne(self)
        self.ship_two = ShipTwo(self)
        self.Bullet = Bullet(self, self.ship_one.i)
        self.bullets = pygame.sprite.Group()
        self.Bullet_two = Bullet_Two(self, self.ship_two.i)
        self.bullets_two = pygame.sprite.Group()

        self.play_game = False
        self.show_instructions = False
        self.show_start = True

        bg_sound = pygame.mixer.Sound('sounds/Doom.mp3')
        bg_sound.play()
        self.m = 0
        self.ded_sound = pygame.mixer.Sound('sounds/scream.wav')
        self.shot_sound = pygame.mixer.Sound('sounds/blaster.mp3')

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.play_game:
                if self.ship_two.health >= -1:
                    if self.ship_one.health >= -1:
                        self.game()
                    else:
                        self.base_font = pygame.font.Font(None, 80)
                        ded_txt = self.base_font.render(self.ded_txt, True, (155, 55, 55))
                        self.screen.blit(ded_txt, (self.txt_rect.x + 700, self.txt_rect.y - 45))
                        pygame.display.flip()
                        if self.m == 0:
                            self.ded_sound.play()
                            self.m += 1
                else:
                    self.base_font = pygame.font.Font(None, 80)
                    ded_txt = self.base_font.render(self.ded_txt, True, (155, 55, 55))
                    self.screen.blit(ded_txt, (self.txt_rect.x, self.txt_rect.y - 45))
                    pygame.display.flip()
                    if self.m == 0:
                        self.ded_sound.play()
                        self.m += 1
            elif self.show_instructions:
                self.instructions()
            elif self.show_start:
                self.start_screen()

    def start_screen(self):
        self.screen.fill((0, 0, 0))
        start = pygame.image.load('images/start_screen.jpg')
        start = pygame.transform.scale(start, (1200, 600))
        self.screen.blit(start, (0, 0))
        strt_txt = self.base_font.render(self.start_txt, True, (155, 55, 55))
        self.screen.blit(strt_txt, (self.txt_rect.x, self.txt_rect.y - 75))
        ins_txt = self.base_font.render(self.inst_txt, True, (155, 55, 55))
        self.screen.blit(ins_txt, (self.txt_rect.x, self.txt_rect.y - 45))
        pygame.display.flip()

    def instructions(self):
        self.screen.fill((0, 0, 0))
        start = pygame.image.load('images/start_screen.jpg')
        start = pygame.transform.scale(start, (1200, 600))
        self.screen.blit(start, (0, 0))
        text_surface = self.base_font.render(self.P_one_instruction_txt, True, (155, 155, 155))
        self.screen.blit(text_surface, (self.txt_rect.x, self.txt_rect.y - 75))
        text_surface_two = self.base_font.render(self.P_two_instruction_txt, True, (155, 155, 155))
        self.screen.blit(text_surface_two, (self.txt_rect.x, self.txt_rect.y - 45))
        text_surface_three = self.base_font.render(self.Rules_txt, True, (155, 155, 155))
        self.screen.blit(text_surface_three, (self.txt_rect.x, self.txt_rect.y - 15))
        text_surface_four = self.base_font.render(self.Rules_two_txt, True, (155, 155, 155))
        self.screen.blit(text_surface_four, (self.txt_rect.x, self.txt_rect.y + 15))
        pygame.display.flip()

    def game(self):
        self._check_events()
        self.ship_one.update()
        self.ship_two.update()
        self._update_bullets()
        self._update_screen()
        self.Bullet.update()
        self.Bullet_two.update()

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
            self._fire_bullet_two()
        if event.key == pygame.K_i:
            self.show_instructions = True
        elif event.key == pygame.K_p:
            self.play_game = True

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
        if event.key == pygame.K_s:
            self._fire_bullet_one()
        if event.key == pygame.K_i:
            self.show_instructions = False
        # Need help adding the stop acceleration for ship two
        # Need help creating the keyup events for ship one using WAD keys

    def _fire_bullet_one(self):
        """Create a new bullet and add it to the bullets group."""
        # Need to split fire mechanic
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self, self.ship_one.i)
            self.bullets.add(new_bullet)
            self.shot_sound.play()

    def _fire_bullet_two(self):
        """Create a new bullet and add it to the bullets group."""
        # Need to split fire mechanic
        if len(self.bullets_two) < self.settings.bullets_allowed:
            new_bullet = Bullet_Two(self, self.ship_two.i)
            self.bullets_two.add(new_bullet)
            self.shot_sound.play()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        self.bullets_two.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets_two.copy():
            if self.are_circles_intersecting(bullet.rect.x, bullet.rect.y, self.settings.bullet_radius,
                                             self.ship_one.rect.x + 20, self.ship_one.rect.y + 20,
                                             self.settings.shield_r):
                self.bullets_two.remove(bullet)
                self.ship_one.health -= 1
            if bullet.rect.y <= 0:  # Need to change this so it removes at any edge
                self.bullets_two.remove(bullet)
            if bullet.rect.x <= 0:  # Need to change this so it removes at any edge
                self.bullets_two.remove(bullet)
            if bullet.rect.y >= 800:  # Need to change this so it removes at any edge
                self.bullets_two.remove(bullet)
            if bullet.rect.x >= 1200:  # Need to change this so it removes at any edge
                self.bullets_two.remove(bullet)

        for bullet in self.bullets.copy():
            if self.are_circles_intersecting(bullet.rect.x, bullet.rect.y, self.settings.bullet_radius,
                                             self.ship_two.rect.x + 20, self.ship_two.rect.y + 20,
                                             self.settings.shield_r):
                self.bullets.remove(bullet)
                self.ship_two.health -= 1
            if bullet.rect.y <= 0:  # Need to change this so it removes at any edge
                self.bullets.remove(bullet)
            if bullet.rect.x <= 0:  # Need to change this so it removes at any edge
                self.bullets.remove(bullet)
            if bullet.rect.y >= 800:  # Need to change this so it removes at any edge
                self.bullets.remove(bullet)
            if bullet.rect.x >= 1200:  # Need to change this so it removes at any edge
                self.bullets.remove(bullet)

    def are_circles_intersecting(self, a_x, a_y, a_radius, b_x, b_y, b_radius):
        return (a_x - b_x) ** 2 + (a_y - b_y) ** 2 <= (a_radius + b_radius) ** 2

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship_one.blitme()
        self.ship_two.blitme()
        self.Bullet.update()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet in self.bullets_two.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    df = Dogfighter()
    df.run_game()
