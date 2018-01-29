import pygame

class Ship():
    def __init__(self,screen):
        self.screen = screen

        #加载飞行物图像 获取外接矩形
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #新飞船放在底部中心
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left  = False

    def update(self):
        """根据移动标志左右移动"""
        if self.moving_right:
            # 向右移动
            self.rect.centerx = min(self.rect.centerx+1 , self.screen_rect.right)
        if self.moving_left:
            # 向右移动
            self.rect.centerx = max(self.rect.centerx-1 , 0)

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)