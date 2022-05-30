class Settings:
    """Клас для збереження всіх налаштувань гри"""

    def __init__(self):
        """Ініціалізувати налаштування гри"""

        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (0, 0, 50)

        # Налаштування корабля
        self.ship_speed = 1
        self.ship_limit = 3

        # Налаштування кулі 1
        self.bullet_speed = 1.5
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (100, 50, 255)
        self.bullets_allowed = 3

        # Налаштування прибульця
        self.alien_speed = 1
        self.fleet_drop_speed = 20
        # fleet_direction 1 означає напрямок руху праворуч; -1 --ліворуч
        self.fleet_direction = 1






        
