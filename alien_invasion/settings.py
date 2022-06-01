import pygame


class Settings:
    """Клас для збереження всіх налаштувань гри"""

    def __init__(self):
        """Ініціалізувати постійні налаштування гри"""

        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (0, 0, 0)
        self.background_image = pygame.image.load('images/background.bmp')


        # Налаштування корабля
        self.ship_limit = 3

        # Налаштування кулі
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (100, 50, 255)
        self.bullets_allowed = 3

        # Налаштування прибульця
        self.fleet_drop_speed = 20

        # Як швидко гра має прискорюватися
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Ініціалізація змінних налаштувань"""
        self.ship_speed = 1
        self.bullet_speed = 1.5
        self.alien_speed = 1

        # fleet_direction 1 означає напрямок руху праворуч; -1 --ліворуч
        self.fleet_direction = 1

    def increase_speed(self):
        """Збільшення налаштувань швидкості"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

