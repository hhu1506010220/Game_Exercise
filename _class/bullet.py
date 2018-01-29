import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,settings,screen,ship):
        # 飞船所在位置初始化子弹
        super(Bullet ,self).__init__()
        self.screen = screen

        # (0,0)设置子弹
        self.rect = pygame.Rect(0,0,settings.bullet_width,settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储小数位
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed = settings.bullet_speed

    def update(self):
        # 子弹向上移动 更新位置
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        # 显示子弹
        pygame.draw.rect(self.screen,self.color,self.rect)
