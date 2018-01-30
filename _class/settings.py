class Settings():
    """存储所有类"""

    def __init__(self):
        """初始化游戏的设置"""

        # 界面
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (100,60,50)

        # 飞船
        self.ship_speed = 1.5
        self.ship_limit = 3

        # 子弹
        self.bullet_speed = 1
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = (150,150,150)

        # 靶子
        self.alien_speed = 1
        self.fleet_drop_speed = 5
        # dir 1为右移 -1为左移
        self.fleet_direction = 1
