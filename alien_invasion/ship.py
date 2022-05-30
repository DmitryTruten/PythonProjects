import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Клас для керування кораблем"""

    def __init__(self, ai_game):
        """Ініціалізувати корабель та задати його початкову позицію"""
        super(Ship, self).__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Завантажити зображення корабля та отримати його rect
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Створювати кожен новий корабель внизу екрана по центру
        self.rect.midbottom = self.screen_rect.midbottom

        # Зберегти десяткове значення для позиції корабля по горизонталі
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Індикатор руху
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        """Оновити поточну позицію корабля на основі
        індикатора руху"""
        # Оновити значення ship.x but not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        elif self.moving_top and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed

        elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        """Відцентрувати корабель на екрані"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Намалювати корабель у його поточному розташуванні"""
        self.screen.blit(self.image, self.rect)
