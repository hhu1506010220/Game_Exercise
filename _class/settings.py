class Settings():
    """存储所有类"""

    def __init__(self):
        """初始化游戏的设置"""

        # 界面
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (50,50,50)

        # 飞船
        self.ship_speed = 1.5

        # 子弹
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (150,150,150)