import sys
import pygame

def check_keydown_events(event,ship):
    # 按下
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event,ship):
    # 松开
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(settings , screen , ship):
    # 刷新屏幕
    screen.fill(settings.bg_color)
    # 展示飞行物
    ship.blitme()
    # 设为可见
    pygame.display.flip()

