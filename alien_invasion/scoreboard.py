import pygame.font


class Scoreboard:
    """Клас, що виводить рахунок"""

    def __init__(self, ai_game):
        """Ініціалізація атрибутів повязаних із рахунком"""
        self.score_rect = None
        self.score_image = None
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Налаштування шрифту для відображення рахунку
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Підготувати зображення з початковим рахунком
        self.prep_score()

    def prep_score(self):
        """Перетворити рахунок на зображення"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Показати рахунок у верхньому правому куты екрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Показати рахунок """
        self.screen.blit(self.score_image, self.score_rect)
