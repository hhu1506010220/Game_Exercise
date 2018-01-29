import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,settings,screen):
        # 初始化靶子
        super(Alien,self).__init__()
        self.screen = screen
        self.settings = settings

        # 加载靶子图像
        self.image = pygame.image.load('image/zsm.bmp')
        self.rect = self.image.get_rect()

        # 初始化位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 浮点数位置
        self.x = float(self.rect.x)

    def blitme(self):
        # 显示靶子
        self.screen.blit(self.image , self.rect)