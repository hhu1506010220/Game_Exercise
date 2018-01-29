import sys
import pygame
from ._class.settings import Settings

def run_game():
    pygame.init()

    #设置样式
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width,settings.screen_height)
    )
    pygame.display.set_caption("雷电")


    # 开始游戏
    while True:

            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #刷新屏幕
            screen.fill(settings.bg_color)

            #设为可见
            pygame.display.flip()

run_game()