import pygame

class Settings:
    def __init__(self):
        # Default fixed window size
        self.default_width = 192 * 3
        self.default_height = 108 * 3

        # Current screen size (start with default)
        self.screen_width = self.default_width
        self.screen_height = self.default_height

        # Background color
        self.bg_color = (230, 230, 230)

        # Clock
        self.clock = pygame.time.Clock()

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 7
