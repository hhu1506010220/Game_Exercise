import pygame

class Settings():
    """存储所有类"""

    def __init__(self):
        """初始化游戏的设置"""

        # 界面
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (100,60,50)
        self.background_image = "image/background.bmp"
        self.background = pygame.image.load(self.background_image)

        # 飞船
        self.ship_speed = 10
        self.ship_limit = 3

        # 子弹
        self.bullet_speed = 10
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = (150,150,150)

        # 靶子
        self.alien_speed = 10
        self.fleet_drop_speed = 10
        # dir 1为右移 -1为左移
        self.fleet_direction = 1

        # 游戏加速
        self.speed_up = 1.2
        self.alien_score = 1.5
        self.init_speed()

    def init_speed(self):
        self.ship_speed = 10
        self.bullet_speed = 10
        self.alien_speed = 10
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speed_up
        self.bullet_speed *= self.speed_up
        self.alien_speed *= self.speed_up
        self.alien_points = int(self.alien_points * self.alien_score)
        print(self.alien_points)