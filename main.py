import pygame
from _class.settings import *
from _class.ship import *
from _class.game_status import *
from _class.button import *
from _class.scoreboard import *
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

    status = GameStatus(settings)
    play_button = Button(settings,screen,"Play")
    ship = Ship(screen,settings)
    bullets = Group()
    aliens =  Group()
    scoreboard = Scoreboard(settings,screen,status)
    func.create_fleet(settings,screen,ship,aliens)

    # 开始游戏
    while True:
        func.check_events(settings,screen,status,play_button,ship,aliens,bullets)

        if status.game_active:
            ship.update()
            bullets.update()
            func.del_bullet(settings,screen,status,scoreboard,ship,aliens,bullets)
            func.update_aliens(settings,status,screen,ship,aliens,bullets)

        func.update_screen(settings,screen,status,scoreboard,ship,aliens,bullets,play_button)

run_game()