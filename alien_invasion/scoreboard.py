import pygame.font
from pygame.sprite import Group
from ship import SmallShip
from ship import Ship
from alien import Alien


class Scoreboard:
    """Клас, що виводить рахунок"""

    def __init__(self, ai_game):
        """Ініціалізація атрибутів повязаних із рахунком"""
        self.ships = None
        self.level_rect = None
        self.level_image = None
        self.high_score_rect = None
        self.high_score_image = None
        self.score_rect = None
        self.score_image = None

        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Налаштування шрифту для відображення рахунку
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 40)

        # Підготувати зображення початкового рахунку
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Перетворити рахунок на зображення"""
        rounded_score = round(self.stats.score, -1)
        score_str = "Score: " + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Показати рахунок у верхньому правому куті екрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Згенерувати рекорд у зображення"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "Highscore: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color)

        # Відцентрувати рекорд по горизонталі
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Перетворити рівень у зображення"""
        level_str = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(level_str,
                                            True, self.text_color)

        # Розташувати рівень над рахунком
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Показує скільки лишилося кораблів"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = SmallShip(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = self.screen_rect.centerx
            self.ships.add(ship)

    def check_high_score(self):
        """Перевірити чи встановлено новий рекорд"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Показати рахунок, кораблі та рівень на екрані"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
