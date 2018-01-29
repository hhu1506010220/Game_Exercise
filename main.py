import sys
import pygame
from _class.settings import Settings
from _class.ship import Ship
import game_function as func

def run_game():
    pygame.init()

    #设置样式
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width,settings.screen_height)
    )
    pygame.display.set_caption("雷电")

    ship = Ship(screen)

    # 开始游戏
    while True:
            func.check_events(ship)
            ship.update()
            func.update_screen(settings,screen,ship)

run_game()