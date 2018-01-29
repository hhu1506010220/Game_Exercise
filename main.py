import sys
import pygame
from _class.settings import Settings
from _class.ship import Ship
import game_function as func
from pygame.sprite import Group

def run_game():
    pygame.init()

    #设置样式
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width,settings.screen_height)
    )
    pygame.display.set_caption("雷电")

    ship = Ship(screen,settings)
    bullets = Group()

    # 开始游戏
    while True:
        func.check_events(settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        func.del_bullet(bullets)
        func.update_screen(settings,screen,ship,bullets)

run_game()