import pygame

class Ship():
    def __init__(self,screen,settings):
        self.screen = screen
        self.settings = settings

        #加载飞行物图像 获取外接矩形
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #新飞船放在底部中心
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.moving_right = False
        self.moving_left  = False
        self.moving_down = False
        self.moving_up = False

        # 设置存储小数值
        self.center = float(self.rect.centerx)
        # self.y = float(self.rect.y)

    def update(self):
        """根据移动标志左右移动"""
        if self.moving_right:
            # 向右移动
            self.center = min(self.center + self.settings.ship_speed , self.screen_rect.right)
        if self.moving_left:
            # 向左移动
            self.center = max(self.center - self.settings.ship_speed , 0)

        # if self.moving_down:
        #     # 向下移动
        #     self.y = max(self.y - self.settings.ship_speed , 0)
        # if self.moving_up:
        #     # 向上移动
        #     self.y = min(self.y + self.settings.ship_speed , self.screen_rect.right)
        # self.rect.y = self.y

        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx